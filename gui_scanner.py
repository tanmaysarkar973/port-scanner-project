import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def start_scan():
    target = entry_ip.get()
    start = int(entry_start.get())
    end = int(entry_end.get())

    result_box.delete(1.0, tk.END)

    def scan(port):
        try:
            s = socket.socket()
            s.settimeout(1)

            if s.connect_ex((target, port)) == 0:
                result_box.insert(tk.END, f"[OPEN] Port {port}\n")

            s.close()
        except:
            pass

    for port in range(start, end + 1):
        threading.Thread(target=scan, args=(port,)).start()


window = tk.Tk()
window.title("Port Scanner")

tk.Label(window, text="Target IP").pack()
entry_ip = tk.Entry(window)
entry_ip.pack()

tk.Label(window, text="Start Port").pack()
entry_start = tk.Entry(window)
entry_start.pack()

tk.Label(window, text="End Port").pack()
entry_end = tk.Entry(window)
entry_end.pack()

tk.Button(window, text="Start Scan", command=start_scan).pack()

result_box = scrolledtext.ScrolledText(window, width=50, height=20)
result_box.pack()

window.mainloop()
