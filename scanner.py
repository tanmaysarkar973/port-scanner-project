import socket
import threading

target = input("Enter target IP: ")
start = int(input("Start port: "))
end = int(input("End port: "))

print(f"\nScanning {target}...\n")

open_ports = []

def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            print(f"[OPEN] Port {port} ({service})")
            open_ports.append((port, service))

        s.close()
    except:
        pass


threads = []

for port in range(start, end + 1):
    t = threading.Thread(target=scan, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Save results
with open("result.txt", "w") as f:
    for port, service in open_ports:
        f.write(f"Port {port} OPEN ({service})\n")

print("\nScan Complete!")
