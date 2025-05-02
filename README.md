![image](https://github.com/user-attachments/assets/67e437b6-4b70-48ab-9f75-9bb842e0620d)

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

## 🙋 Auteur
Cheick Ousmane BAMBA


LinkedIn : https://www.linkedin.com/in/cheick-ousmane-bamba-258529323

---

## 🧰 Technologies utilisées

- Python 3.x
- [`python-nmap`](https://pypi.org/project/python-nmap/)
- [`fpdf`](https://pyfpdf.github.io/fpdf2/)
- Nmap (doit être installé sur la machine)

---

## 📦 Installation

```bash
git clone https://github.com/cheick-bamba/ethnet-audit.git
cd ethnet-audit
chmod +x setup.sh
./setup.sh
```
---

### ▶️ Utilisation avec génération de rapport en PDF
Active l’environnement virtuel et exécute le script :
```bash
source venv/bin/activate
python main.py
```
L’outil te demandera d’entrer une plage IP à scanner (ex. : 192.168.1.0/24).
Il effectuera ensuite les étapes suivantes :

🔍 Détection des hôtes actifs

🔐 Scan des ports et services pour chaque hôte détecté

🧾 Génération d’un rapport PDF complet

--- 
### ▶️ Utilisation avec génération de rapport en JSON || CSV

``` bash
python main.py --export json
python main.py --export csv
```

### 🛡️ Licence

Ce projet est distribué sous licence MIT. Vous êtes libre de l’utiliser, le modifier et le distribuer.
