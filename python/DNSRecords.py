#!/usr/bin/env python3
import dns.resolver
import dns.exception
import dns.reversename

def resolve_records(domain, records, timeout=2.0, lifetime=5.0):
    resolver = dns.resolver.Resolver()
    resolver.timeout = timeout
    resolver.lifetime = lifetime

    results = {}

    for record in records:
        try:
            # Skip invalid PTR usage
            if record == "PTR":
                results[record] = {"error": "PTR requires reverse lookup name"}
                continue

            answers = resolver.resolve(domain, record)
            values = []

            for r in answers:
                if record == "TXT":
                    values.append(b"".join(r.strings).decode(errors="replace"))
                else:
                    values.append(str(r))

            results[record] = values

        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            results[record] = []
        except (dns.resolver.Timeout, dns.resolver.NoNameservers):
            results[record] = {"error": "timeout or no nameservers"}
        except dns.exception.DNSException:
            results[record] = {"error": "dns error"}

    return results

def main():
    domain = "google.com"
    records = ['A','AAAA','CNAME','MX','NS','SOA','TXT']
    data = resolve_records(domain, records)

    for record, values in data.items():
        print(f"\nRecord response {record}")
        print("-" * 36)
        if isinstance(values, dict):
            print(values["error"])
        elif values:
            for v in values:
                print(v)
        else:
            print("No records found")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit(0)
