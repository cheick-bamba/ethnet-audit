import nmap

def scan_hosts(network_range="192.168.1.0/24"):
    nm = nmap.PortScanner()
    nm.scan(hosts=network_range, arguments="-sn")  # ping scan only
    hosts_up = []

    for host in nm.all_hosts():
        mac = nm[host]['addresses'].get('mac', 'N/A')
        hosts_up.append({
            "ip": host,
            "mac": mac,
            "hostname": nm[host].hostname()
        })

    return hosts_up
