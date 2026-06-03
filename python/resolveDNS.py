#!/usr/bin/env python3
import dns.resolver
import dns.exception

def resolve_dns(hosts, record_types=("A", "AAAA"), timeout=2.0, lifetime=5.0):
    resolver = dns.resolver.Resolver()
    resolver.timeout = timeout
    resolver.lifetime = lifetime

    results = {}
    for host in hosts:
        host_res = {}
        for rtype in record_types:
            try:
                answers = resolver.resolve(host, rtype)
                host_res[rtype] = [str(rdata) for rdata in answers]
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
                host_res[rtype] = []
            except (dns.resolver.Timeout, dns.resolver.NoNameservers) as e:
                host_res[rtype] = {"error": type(e).__name__}
            except dns.exception.DNSException as e:
                host_res[rtype] = {"error": type(e).__name__}
        results[host] = host_res
    return results

def main():
    hosts = ["google.com", "microsoft.com"]
    data = resolve_dns(hosts, record_types=("AAAA",))
    for host, host_res in data.items():
        print(f"\n{host}\n" + "-" * 36)
        v = host_res.get("AAAA", [])
        if isinstance(v, dict) and "error" in v:
            print(f"AAAA error: {v['error']}")
        elif v:
            for item in v:
                print(item)
        else:
            print("No AAAA records")
        print("-" * 36)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit(0)
