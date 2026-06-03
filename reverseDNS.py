#!/usr/bin/env python3
import dns.resolver
import dns.reversename
import dns.exception

def ptr_lookup(ip, timeout=2.0, lifetime=5.0):
    resolver = dns.resolver.Resolver()
    resolver.timeout = timeout
    resolver.lifetime = lifetime

    rev = dns.reversename.from_address(ip)
    try:
        answers = resolver.resolve(rev, "PTR")
        return [str(r).rstrip(".") for r in answers]
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        return []
    except (dns.resolver.Timeout, dns.resolver.NoNameservers, dns.exception.DNSException) as e:
        return {"error": type(e).__name__}

def main():
    ip = "142.250.31.101"
    print("-" * 36)
    print(dns.reversename.from_address(ip))
    res = ptr_lookup(ip)
    print(res)
    print("-" * 36)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit(0)
