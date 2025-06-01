
# 🛒 Shop Management – Application de gestion de boutique (Tkinter)

> Une application bureautique développée en **Python** avec **Tkinter** pour la gestion des ventes, produits et clients d’une boutique. Interface graphique simple, intuitive et autonome.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Tkinter-GUI-blue?style=flat-square" alt="Tkinter"/>
  <img src="https://img.shields.io/badge/Type-Bureautique-orange?style=flat-square" alt="Desktop"/>
  <img src="https://img.shields.io/badge/Status-Terminé-brightgreen?style=flat-square" alt="Status"/>
</p>

---

## Fonctionnalités principales

- Gestion des produits : ajout, modification, suppression
- Gestion des ventes avec facturation automatique
- Suivi des clients
- Sauvegarde automatique des données (fichiers ou base SQLite)
- Interface claire avec formulaires, boutons, et tableaux

---

## Technologies utilisées

| Élément         | Détail                         |
|-----------------|---------------------------------|
| Langage         | Python 3                        |
| Interface       | Tkinter                         |
| Sauvegarde      | Fichier ou base SQLite (local)  |
| Déploiement     | PyInstaller (exécutable .exe)   |

---

## Lancer le projet localement

```bash
# 1. Cloner le dépôt
git clone https://github.com/majoiefaya/Shop-Management.git
cd Shop-Management

# 2. Installer les dépendances (optionnel si standard library)
pip install -r requirements.txt 

# 3. Créer la base de données intitulée : ma_boutique

# 4. Executer le script SQL dans la base de données ma_boutique
le script se trouve dans le fichier :https://github.com/majoiefaya/Shop-Management/blob/main/BASE DE DONNE MA BOUTIQUE.txt

# 5. Lancer l'application
python main.py
```

---

## Capture d’écran

<p align="center">
  <img src="https://github.com/majoiefaya/Shop-Management/blob/main/app_presentation.png?raw=true" width="600" alt="Aperçu application"/>
</p>

---

## 📦 Générer un exécutable (.exe)

> Si tu veux distribuer l’application sans que l’utilisateur n’installe Python :

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

Le fichier `.exe` sera disponible dans le dossier `dist/`.

---

## 📄 Licence

Application personnelle développée par **Faya Lidao Majoie**.  
Utilisation libre à des fins non commerciales.

---

## ☕ Me soutenir

<p align="center">
  <a href="https://buymeacoffee.com/majoiefaya" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat-square&logo=buymeacoffee&logoColor=black" alt="Buy Me a Coffee"/>
  </a>
</p>
