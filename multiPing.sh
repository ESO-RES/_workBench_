#!/bin/bash
FILE="${1}"
while read -r host; do
    #ping -c 1 -W 1 -w 1 "${host}" &> /dev/null; then #linux
    if ping -c 1 -t 1 -W 1 "${host}" &> /dev/null; then #mac
        echo "${host} is active."
    fi
done < "${FILE}"
# nmap -sn 10.211.55.0/24 | grep "Nmap scan" | awk -F'report for ' '{print $2}'
