from scapy.all import IP, TCP, sr1

target = input("Enter target IP: ")
start = int(input("Start port: "))
end = int(input("End port: "))

print(f"\nSYN Scanning {target}...\n")

for port in range(start, end + 1):
    pkt = IP(dst=target)/TCP(dport=port, flags="S")

    response = sr1(pkt, timeout=1, verbose=0)

    if response:
        if response.haslayer(TCP):
            if response[TCP].flags == 18:  # SYN-ACK
                print(f"[OPEN] Port {port}")

                # Send RST to close connection
                rst = IP(dst=target)/TCP(dport=port, flags="R")
                sr1(rst, timeout=1, verbose=0)
