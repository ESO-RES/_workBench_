#!/usr/bin/env python3
import random
# Description of 20 common TCP ports and 20 common UDP ports with a study game
class Protocol:
    def __init__(self, name, number, description):
        self.name = name
        self.number = number
        self.description = description

    def getProtocolInfo(self):
        print()
        print(f"{self.name} - {self.number} - {self.description}")
        print()
# --- GLOBALS
LISTTCP = {
    'FTP': 21, 'SSH': 22, 'TELNET': 23, 'SMTP': 25, 'DNS': 53, 'HTTP': 80, 'POP3': 110, 'RPCBIND': 111,
    'MSRPC': 135, 'NETBIOS SSN': 139, 'IMAP': 143, 'HTTPS': 443, 'MICROSOFT DS': 445, 'IMAPS': 993,
    'POP3S': 995, 'PPTP': 1723, 'MYSQL': 3306, 'MS TERM SERVER': 3389, 'VNC': 5900, 'HTTP PROXY': 8080
}
LISTUDP = {
    'DNS': 53, 'DHCPS': 67, 'DHCPC': 68, 'TFTP': 69, 'NTP': 123, 'MSRPC': 135, 'NETBIOS NS': 137,
    'NETBIOS DGM': 138, 'NETBIOS SSN': 139, 'SNMP': 161, 'SNMPTRAP': 162, 'MICROSOFT DS': 445,
    'ISAKMP': 500, 'SYSLOG': 514, 'RIP': 520, 'IPP': 631, 'MS SQL DS': 1434, 'UPNP': 1900,
    'NAT T IKE': 4500, 'VARIES': 49152
}
def main():
    print()
    questionUser()
def questionUser():
    count = 0
    while count <= 3:
        print('-' * 23)
        ask = input("(G)ame? (Q)uit?\nUDP or TCP ports? ").strip().lower()
        if ask == "tcp":
            print('-' * 23)
            tcpPorts()
        elif ask == "udp":
            print('-' * 23)
            udpPorts()
        elif ask in ("game", "g"):
            callGame()
        elif ask in ("q", "quit"):
            print('-' * 23)
            raise SystemExit(0)
        else:
            print("Incorrect input. Try again.")
            count += 1
def tcpPorts():
    ftp = Protocol("FTP", 21, "File Transfer Protocol")
    ssh = Protocol("SSH", 22, "Secure Shell")
    telnet = Protocol("TELNET", 23, "Client/Server Protocol")
    smtp = Protocol("SMTP", 25, "Simple Mail Transfer Protocol")
    dns = Protocol("DNS", 53, "Domain Name Server")
    http = Protocol("HTTP", 80, "Hypertext Transfer Protocol (Unsecured)")
    pop3 = Protocol("POP3", 110, "Post Office Protocol Version 3 for email retrieval (insecure)")
    rpcBIND = Protocol("RPCBIND", 111, "Maps SunRPC program numbers to their current TCP or UDP ports")
    msRPC = Protocol("MSRPC", 135, "Common Port For Windows Services")
    netBIOSSNN = Protocol("NetBIOS SSN", 139, "Communications for NetBIOS Session Service")
    imap = Protocol("IMAP", 143, "Internet Message Access Protocol version 2")
    https = Protocol("HTTPS", 443, "Hypertext Transfer Protocol Secured")
    msDS = Protocol("MICROSOFT DS", 445, "SMB Over IP With Windows services")
    imaps = Protocol("IMAPS", 993, "IMAP over SSL/TLS")
    pop3S = Protocol("POP3S", 995, "POP3 over SSL/TLS")
    pptp = Protocol("PPTP", 1723, "Point To Point Tunneling Protocol")
    mySQL = Protocol("MySQL", 3306, "Communication with MySQL databases")
    msTermServer = Protocol("MS TERM SERVER", 3389, "Microsoft Terminal Services port")
    vnc = Protocol("VNC", 5900, "A Graphical Desktop Sharing System")
    httpProxy = Protocol("HTTP PROXY", 8080, "Commonly Used For HTTP Proxies")
    count = 0
    while count <= 3:
        answer = input("(B)ack? (L)ist? (Q)uit?\n-- Which TCP protocol: ").strip().lower()
        if answer == "ftp" or answer == "21":
            ftp.getProtocolInfo(); count = 0
        elif answer == "ssh" or answer == "22":
            ssh.getProtocolInfo(); count = 0
        elif answer == "telnet" or answer == "23":
            telnet.getProtocolInfo(); count = 0
        elif answer == "smtp" or answer == "25":
            smtp.getProtocolInfo(); count = 0
        elif answer == "dns" or answer == "53":
            dns.getProtocolInfo(); count = 0
        elif answer == "http" or answer == "80":
            http.getProtocolInfo(); count = 0
        elif answer in ("pop3", "pop 3") or answer == "110":
            pop3.getProtocolInfo(); count = 0
        elif answer in ("rpc-bind", "rpcbind") or answer == "111":
            rpcBIND.getProtocolInfo(); count = 0
        elif answer == "msrpc" or answer == "135":
            msRPC.getProtocolInfo(); count = 0
        elif answer in ("netbios-ssn", "netbios_ssn", "netbios ssn", "netbiosssn", "netbiossnn") or answer == "139":
            netBIOSSNN.getProtocolInfo(); count = 0
        elif answer == "imap" or answer == "143":
            imap.getProtocolInfo(); count = 0
        elif answer == "https" or answer == "443":
            https.getProtocolInfo(); count = 0
        elif answer in ("microsoft-ds", "microsoft_ds", "microsoft ds", "microsoftds") or answer == "445":
            msDS.getProtocolInfo(); count = 0
        elif answer in ("imaps", "993"):
            imaps.getProtocolInfo(); count = 0
        elif answer in ("pop3s", "pop ssl", "995"):
            pop3S.getProtocolInfo(); count = 0
        elif answer == "pptp" or answer == "1723":
            pptp.getProtocolInfo(); count = 0
        elif answer in ("my-sql", "my_sql", "my sql", "mysql") or answer == "3306":
            mySQL.getProtocolInfo(); count = 0
        elif answer in ("ms-term-server", "ms_term_server", "ms term server", "mstermserver") or answer == "3389":
            msTermServer.getProtocolInfo(); count = 0
        elif answer == "vnc" or answer == "5900":
            vnc.getProtocolInfo(); count = 0
        elif answer in ("http-proxy", "http_proxy", "http proxy", "httpproxy") or answer == "8080":
            httpProxy.getProtocolInfo(); count = 0
        elif answer in ("b", "back"):
            return
        elif answer in ("list", "l"):
            print()
            for key, value in LISTTCP.items():
                print(key, value)
            print()
        elif answer in ("q", "quit"):
            print('-' * 23)
            raise SystemExit(0)
        else:
            print("Incorrect input. Try again")
            count += 1
def udpPorts():
    dns_p = Protocol("DNS", 53, "Domain Name Systems Server")
    dhcps = Protocol("DHCPS", 67, "Dynamic Host Configuration Protocol Server")
    dhcpc = Protocol("DHCPC", 68, "DHCP Client port")
    tftp = Protocol("TFTP", 69, "Trivial File Transfer Protocol")
    ntp = Protocol("NTP", 123, "Network Time Protocol")
    msRPC = Protocol("MSRPC", 135, "Windows Services Port")
    netBIOSNS = Protocol("NETBIOS NS", 137, "UDP Port For Windows")
    netBIOSDGM = Protocol("NETBIOS DGM", 138, "Another Windows Service")
    netBIOSSSN = Protocol("NETBIOS SSN", 139, "Another Windows Service")
    snmp = Protocol("SNMP", 161, "Simple Network Manage Protocol")
    snmpTrap = Protocol("SNMPTRAP", 162, "Simple Network Management Protocol")
    msDS = Protocol("MICROSOFT DS", 445, "Windows Services Port")
    isakmp = Protocol("ISAKMP", 500, "Internet Security Association And Key Management")
    sysLog = Protocol("SYSLOG", 514, "Standard UNIX Log Daemon")
    rip = Protocol("RIP", 520, "Routing Information Protocol")
    ipp = Protocol("IPP", 631, "Internet Printing Protocol")
    msSQLDS = Protocol("MS SQL DS", 1434, "Microsoft SQL Browser/Discovery")
    upnp = Protocol("UPNP", 1900, "Simple Service Discovery Protocol (SSDP)")
    natTIKE = Protocol("NAT T IKE", 4500, "NAT traversal during IPsec IKE")
    ephemeral = Protocol("Varies", 49152, "Start of IANA dynamic/private (ephemeral) range")
    count = 0
    while count <= 3:
        answer = input("(B)ack? (L)ist? (Q)uit?\n-- Which UDP protocol: ").strip().lower()
        if answer == "dns" or answer == "53":
            dns_p.getProtocolInfo(); count = 0
        elif answer == "dhcps" or answer == "67":
            dhcps.getProtocolInfo(); count = 0
        elif answer == "dhcpc" or answer == "68":
            dhcpc.getProtocolInfo(); count = 0
        elif answer == "tftp" or answer == "69":
            tftp.getProtocolInfo(); count = 0
        elif answer == "ntp" or answer == "123":
            ntp.getProtocolInfo(); count = 0
        elif answer == "msrpc" or answer == "135":
            msRPC.getProtocolInfo(); count = 0
        elif answer in ("netbios ns", "netbiosns") or answer == "137":
            netBIOSNS.getProtocolInfo(); count = 0
        elif answer in ("netbios dgm", "netbiosdgm") or answer == "138":
            netBIOSDGM.getProtocolInfo(); count = 0
        elif answer in ("netbios ssn", "netbiosssn") or answer == "139":
            netBIOSSSN.getProtocolInfo(); count = 0
        elif answer == "snmp" or answer == "161":
            snmp.getProtocolInfo(); count = 0
        elif answer == "snmptrap" or answer == "162":
            snmpTrap.getProtocolInfo(); count = 0
        elif answer in ("msds", "microsoft ds", "microsoft-ds") or answer == "445":
            msDS.getProtocolInfo(); count = 0
        elif answer == "isakmp" or answer == "500":
            isakmp.getProtocolInfo(); count = 0
        elif answer == "syslog" or answer == "514":
            sysLog.getProtocolInfo(); count = 0
        elif answer == "rip" or answer == "520":
            rip.getProtocolInfo(); count = 0
        elif answer == "ipp" or answer == "631":
            ipp.getProtocolInfo(); count = 0
        elif answer in ("ms sql ds", "mssql ds", "mssql") or answer == "1434":
            msSQLDS.getProtocolInfo(); count = 0
        elif answer == "upnp" or answer == "1900":
            upnp.getProtocolInfo(); count = 0
        elif answer in ("nat t ike", "natt ike", "nat-t ike") or answer == "4500":
            natTIKE.getProtocolInfo(); count = 0
        elif answer in ("ephemeral", "varies") or answer == "49152":
            ephemeral.getProtocolInfo(); count = 0
        elif answer in ("b", "back"):
            return
        elif answer in ("list", "l"):
            print()
            for key, value in LISTUDP.items():
                print(key, value)
            print()
        elif answer in ("q", "quit"):
            print('-' * 23)
            raise SystemExit(0)
        else:
            print("Incorrect input. Try again")
            count += 1
def _normalize(s: str) -> str:
    """Normalize user input for loose matching."""
    return " ".join(s.strip().lower().replace("_", " ").replace("-", " ").split())
def callGame():
    """
    Point system:
      +1 point for correct answer (by name, e.g., 'dns', or by port number if user types it back)
      0 points for incorrect
    Session score resets each time you enter Game mode.
    """
    score = 0
    total = 0
    # Precompute normalized lookup maps for faster and looser matching.
    tcp_name_by_port = {v: k for k, v in LISTTCP.items()}
    udp_name_by_port = {v: k for k, v in LISTUDP.items()}
    tcp_norm_to_name = {_normalize(k): k for k in LISTTCP.keys()}
    udp_norm_to_name = {_normalize(k): k for k in LISTUDP.keys()}
    while True:
        print()
        print(f"Score: {score}/{total}")
        ask = input("(P)lay? (R)eset score? (B)ack?\n").strip().lower()
        if ask in ("p", "play"):
            total += 1
            tcpUDP = random.randint(1, 2)
            if tcpUDP == 1:
                question_port = random.choice(list(LISTTCP.values()))
                correct_name = tcp_name_by_port[question_port]
                user = input(f"What is TCP port {question_port}? ").strip()
                # Accept either correct name (loose) OR the correct port typed back.
                user_norm = _normalize(user)
                is_correct = (
                    user_norm == _normalize(correct_name)
                    or (user.strip().isdigit() and int(user.strip()) == question_port)
                )

                if is_correct:
                    score += 1
                    print("Correct.")
                else:
                    print(f"Incorrect. Answer: {correct_name}.")
            else:
                question_port = random.choice(list(LISTUDP.values()))
                correct_name = udp_name_by_port[question_port]
                user = input(f"What is UDP port {question_port}? ").strip()

                user_norm = _normalize(user)
                is_correct = (
                    user_norm == _normalize(correct_name)
                    or (user.strip().isdigit() and int(user.strip()) == question_port)
                )
                if is_correct:
                    score += 1
                    print("Correct.")
                else:
                    print(f"Incorrect. Answer: {correct_name}.")
        elif ask in ("r", "reset"):
            score = 0
            total = 0
            print("Score reset.")
        elif ask in ("b", "back"):
            return
        else:
            print("Incorrect input. Try again")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit(0)
