# 🛡️ ETHNET-AUDIT

**ETHNET-AUDIT** est un outil Python open-source d’audit de sécurité pour réseaux locaux. Il permet de détecter les hôtes actifs, d’identifier les ports ouverts, d’analyser les services exposés, et de générer automatiquement un **rapport PDF** ainsi que des **exports JSON/CSV**.

---

## 🚀 Fonctionnalités

- 🔎 Scan des hôtes actifs sur une plage IP donnée
- 🔐 Scan des ports ouverts et services associés
- 📄 Génération automatique d’un **rapport PDF** clair et structuré
- 📁 Export des résultats en **JSON** ou **CSV**
- ✅ Utilisation simple en ligne de commande

---

## 🧰 Technologies utilisées

- Python 3.x
- [`python-nmap`](https://pypi.org/project/python-nmap/)
- [`fpdf`](https://pyfpdf.github.io/fpdf2/)
- Nmap (doit être installé sur la machine)

---

## 📦 Installation

```bash
git clone https://github.com/votre-utilisateur/ethnet-audit.git
cd ethnet-audit
chmod +x setup.sh
./setup.sh
