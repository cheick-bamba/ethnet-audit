import argparse
from scanner import scan_hosts
from port_scanner import scan_ports
from rapport_pdf import PDFReport
from datetime import datetime
import json
import csv

def export_json(hosts, filename):
    with open(filename, 'w') as f:
        json.dump(hosts, f, indent=4)
    print(f"[✔] Fichier JSON exporté : {filename}")

def export_csv(hosts, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['ip', 'hostname', 'mac', 'port', 'service', 'product', 'version']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for host in hosts:
            if host['ports']:
                for port in host['ports']:
                    writer.writerow({
                        'ip': host['ip'],
                        'hostname': host['hostname'],
                        'mac': host['mac'],
                        'port': port['port'],
                        'service': port['service'],
                        'product': port['product'],
                        'version': port['version']
                    })
            else:
                writer.writerow({
                    'ip': host['ip'],
                    'hostname': host['hostname'],
                    'mac': host['mac'],
                    'port': '',
                    'service': '',
                    'product': '',
                    'version': ''
                })
    print(f"[✔] Fichier CSV exporté : {filename}")

def main():
    parser = argparse.ArgumentParser(description="ETHNET-AUDIT - Outil d'audit réseau local")
    parser.add_argument("--export", choices=["json", "csv"], help="Exporter les résultats en JSON ou CSV")
    args = parser.parse_args()

    print("=== ETHNET-AUDIT - Détection des hôtes et scan de ports ===")
    ip_range = input("Entrez la plage IP à scanner (ex: 192.168.1.0/24) : ").strip()

    if not ip_range:
        print("[!] Aucune plage saisie. Abandon.")
        return

    hosts = scan_hosts(ip_range)
    print(f"\n[+] {len(hosts)} hôte(s) détecté(s).")

    for host in hosts:
        print(f"\n--- Hôte : {host['ip']} ({host['hostname']}) ---")
        port_results = scan_ports(host["ip"])
        host["ports"] = port_results

        if not port_results:
            print("  Aucun port ouvert détecté.")
        else:
            for p in port_results:
                print(f"  Port {p['port']} : {p['service']} ({p['product']} {p['version']})")

    # Génération du PDF
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    pdf_name = f"rapport_ethnet_audit_{timestamp}.pdf"
    print("\n[📄] Génération du rapport PDF...")
    pdf = PDFReport()
    pdf.add_page()
    for host in hosts:
        pdf.add_host(host)
    pdf.output(pdf_name)
    print(f"[✔] Rapport généré : {pdf_name}")

    # Export JSON ou CSV si demandé
    if args.export == "json":
        export_json(hosts, f"ethnet_audit_{timestamp}.json")
    elif args.export == "csv":
        export_csv(hosts, f"ethnet_audit_{timestamp}.csv")

if __name__ == "__main__":
    main()
