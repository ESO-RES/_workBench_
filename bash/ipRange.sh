#!/bin/bash
#Generate IP address from a specific range
#[./ipRange.sh 10.211.55]
ADDRESS="${1}"
for ip in $(seq 1 254); do
    echo "${ADDRESS}.${ip}" >> ipRangeList.txt
done
#printf "10.211.55.%d\n" {1..255} >> ipRangeList.txt
