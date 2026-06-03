#!/usr/bin/env python3
# Example run:
#   python3 socketPortScan.py -H scanme.nmap.org -P 1-1024,8080,8443
#   python3 socketPortScan.py -H 192.168.1.1 -P 22,80,443 --timeout 1 --workers 50
import argparse
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
def parse_ports(port_str: str) -> list[int]:
    """
    Parse ports from a string supporting:
      - Single ports: 22
      - Ranges: 1-1024
      - Mixed lists: 1-1024,8080,8443
    """
    ports: set[int] = set()
    for token in port_str.split(","):
        token = token.strip()
        if not token:
            continue
        # Handle ranges like 1-1024
        if "-" in token:
            start, end = token.split("-", 1)
            if not start.isdigit() or not end.isdigit():
                raise ValueError(f"Invalid port range: {token}")
            start_p = int(start)
            end_p = int(end)
            if start_p > end_p:
                raise ValueError(f"Invalid port range (start > end): {token}")
            for p in range(start_p, end_p + 1):
                if not (1 <= p <= 65535):
                    raise ValueError(f"Port out of range: {p}")
                ports.add(p)
        # Handle single ports
        else:
            if not token.isdigit():
                raise ValueError(f"Invalid port: {token}")
            p = int(token)
            if not (1 <= p <= 65535):
                raise ValueError(f"Port out of range: {p}")
            ports.add(p)
    if not ports:
        raise ValueError("No ports provided")
    return sorted(ports)
def scan_port(ip: str, port: int, timeout: float) -> tuple[int, bool, str]:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            rc = s.connect_ex((ip, port))  # 0=open, else error
            if rc == 0:
                return (port, True, "open")
            return (port, False, "closed")
    except socket.gaierror:
        return (port, False, "name resolution error")
    except socket.timeout:
        return (port, False, "timeout")
    except OSError as e:
        return (port, False, f"os error: {e.__class__.__name__}")
def port_scan(host: str, ports: list[int], timeout: float = 1.5, workers: int = 100) -> None:
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"[-] Cannot resolve '{host}': Unknown host")
        return
    try:
        name = socket.gethostbyaddr(ip)[0]
        print(f"[+] Scan Results for: {ip} {name}")
    except OSError:
        print(f"[+] Scan Results for: {ip}")
    workers = max(1, min(workers, len(ports)))
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(scan_port, ip, p, timeout): p for p in ports}
        for fut in as_completed(futures):
            port, is_open, msg = fut.result()
            if is_open:
                print(f"[+] {port}/tcp open")
            else:
                print(f"[-] {port}/tcp {msg}")
def main():
    parser = argparse.ArgumentParser(
        prog="socketPortScan",
        description="TCP port scanner (authorized use only).",
    )
    parser.add_argument("-H", "--host", required=True, help="Target host (DNS name or IPv4)")
    parser.add_argument(
        "-P",
        "--ports",
        required=True,
        help="Ports (e.g. 22,80,443 or 1-1024,8080)",
    )
    parser.add_argument("--timeout", type=float, default=1.5, help="Socket timeout seconds (default: 1.5)")
    parser.add_argument("--workers", type=int, default=100, help="Max concurrent threads (default: 100)")
    args = parser.parse_args()
    ports = parse_ports(args.ports)
    port_scan(args.host, ports, timeout=args.timeout, workers=args.workers)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit(0)
