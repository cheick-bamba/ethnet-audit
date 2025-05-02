#!/bin/bash

echo "[*] Installation de l'environnement virtuel..."
python3 -m venv venv
source venv/bin/activate

echo "[*] Installation des dépendances..."
pip install -r requirements.txt

echo "[✔] Installation terminée. Pour lancer l’outil :"
echo "source venv/bin/activate && python main.py"
