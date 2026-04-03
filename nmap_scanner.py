import nmap

target = input("Enter target IP: ")

scanner = nmap.PortScanner()

print(f"\nScanning {target} using Nmap...\n")

scanner.scan(target, '1-1000')

for host in scanner.all_hosts():
    print(f"Host: {host}")

    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()

        for port in ports:
            state = scanner[host][proto][port]['state']
            service = scanner[host][proto][port]['name']

            print(f"[{state.upper()}] Port {port} ({service})")
