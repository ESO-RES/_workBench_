#!/bin/bash
#TCP connect scan on target
# [./bashPort.sh 192.168.10.1]
TARGET="$1"
PORTS="22 23 25 53 80 110 143 443 445 3389 8080 8443"
for p in $PORTS; do
	if (echo > /dev/tcp/$TARGET/$p) > /dev/null 2>&1; then
		echo "[+] Port $p open"
	else
		echo "[-] Port $p closed"
	fi
done
# nmap -sT <target IP>
