
import sys
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

class ScannerPort:
    
    def __init__(self, host, ports):
        self.host = host
        self.ports = self.parse_ports(ports)
    
    def start(self):
        with ThreadPoolExecutor() as executor:
            executor.map(self.ports_scan, self.ports)
    
    def ports_scan(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #TCP
                s.settimeout(1)
                s.connect((self.host,port))
                s.sendall(b"HEAD / HTTP/1.1\r\n\r\n")
                response = s.recv(1024).decode(errors="ignore").split("\n")[0]
                if response and any(c.isprintable() for c in response):
                    print(f"\t\t[+] Port: {port} - OPEN > {response}")
                else:
                    print(f"\t\t[+] Port: {port} - OPEN")
        except (socket.timeout, ConnectionRefusedError):
            pass
    
    def parse_ports(self, ports_str):
        try:
            if '-' in ports_str:
                port_range = [int(p) for p in ports_str.split("-")]
                return range(port_range[0], port_range[1]+1)
            elif ',' in ports_str:
                return map(int, ports_str.split(","))
            else:
                return [int(ports_str)]
        except Exception:
            print("[-] Range port invalid")
            sys.exit(1)