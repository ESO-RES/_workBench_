#!/bin/bash
echo -e work-{0..100}.{txt,csv,pdf,jpg}"\n" | sed 's/ //g' > genFilesList.txt
# ffuf -c -w genFilesList.txt -u http://10.0.100.10:8081/files/FUZZ
# wfuzz --sc 200 -w genFilesList.txt http://10.0.100.10:8081/files/FUZZ
