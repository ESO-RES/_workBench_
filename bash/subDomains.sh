#!/bin/bash
#Create possible subdomains 
#[./subDomains.sh test.com subDomains.txt]
DOMAIN="${1}"
FILE="${2}"
while read -r subdomain; do
    echo "${subdomain}.${DOMAIN}" >> subDomainsList.txt
done < "${FILE}"
#sed 's/$/.example.com/g' subDomains.txt >> subDomainsList.txt
