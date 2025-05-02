from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'ETHNET-AUDIT - Rapport de Scan Réseau', ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_host(self, host):
        self.set_font('Arial', 'B', 11)
        self.cell(0, 10, f"Hôte : {host['ip']} ({host['hostname']})", ln=True)
        self.set_font('Arial', '', 10)
        self.cell(0, 10, f"MAC : {host['mac']}", ln=True)

        if not host["ports"]:
            self.cell(0, 10, "  Aucun port ouvert détecté.", ln=True)
        else:
            self.set_font('Arial', 'B', 10)
            self.cell(0, 8, "  Ports ouverts :", ln=True)
            self.set_font('Arial', '', 10)
            for p in host["ports"]:
                self.cell(0, 8,
                          f"    - Port {p['port']} : {p['service']} ({p['product']} {p['version']})", ln=True)
        self.ln(5)
