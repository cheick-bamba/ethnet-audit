import nmap

def scan_ports(ip, ports="1-1024"):
    nm = nmap.PortScanner()
    print(f"\n[*] Scan des ports sur {ip}...")
    nm.scan(ip, ports, arguments="-sV")
    results = []

    if ip in nm.all_hosts():
        for proto in nm[ip].all_protocols():
            lport = nm[ip][proto].keys()
            for port in sorted(lport):
                service = nm[ip][proto][port].get('name', 'unknown')
                product = nm[ip][proto][port].get('product', '')
                version = nm[ip][proto][port].get('version', '')
                results.append({
                    "port": port,
                    "service": service,
                    "product": product,
                    "version": version
                })
    return results
