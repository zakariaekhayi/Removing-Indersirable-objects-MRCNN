# Removing-Undesirable-Objects-MRCNN

Ce projet vise à supprimer des objets indésirables d'une image. Il permet aux utilisateurs de sélectionner un objet sur une photo pour le supprimer automatiquement en utilisant des techniques avancées comme la segmentation instancielle (**Mask R-CNN**) et le remplissage basé sur l'inpainting.

---

## Description

Le projet utilise **Mask R-CNN** pour détecter et segmenter les objets dans une image. Une fois l'objet sélectionné, il est automatiquement supprimé et la région vide est complétée à l'aide de l'inpainting.

### Techniques Utilisées :

- **Segmentation instancielle (Mask R-CNN)**
- **Inpainting** pour remplir les zones supprimées.

---

## Prérequis

1. **Python 3.7** : Assurez-vous que cette version est installée.
2. **Git** : Pour télécharger les fichiers requis.
3. **Mask R-CNN Repository** : Le projet dépend de la bibliothèque Mask R-CNN disponible sur GitHub.

---

## Instructions d'Installation et d'Exécution

### 1. Cloner et Configurer le Repository Mask R-CNN

- Téléchargez le repository **Mask R-CNN** à partir du lien suivant :
  [https://github.com/matterport/Mask\_RCNN.git](https://github.com/matterport/Mask_RCNN.git)

- Extrayez le contenu du repository et placez-le **dans le même emplacement** que le fichier `rcnn.py` de votre projet.

### 2. Télécharger le Modèle COCO Pré-entrainé

- Téléchargez le fichier **mask\_rcnn\_coco.h5** à partir du lien suivant :
  [https://github.com/matterport/Mask\_RCNN/releases](https://github.com/matterport/Mask_RCNN/releases)

- Placez le fichier **mask\_rcnn\_coco.h5** dans le dossier du projet.

### 3. Installation de Python 3.7 et Configuration de l'Environnement Virtuel

1. **Installer Python 3.7** : Téléchargez et installez Python 3.7 à partir du site officiel.

   - Assurez-vous d'ajouter Python au PATH lors de l'installation.

2. **Créer un environnement virtuel** :

   - Ouvrez PowerShell ou CMD.
   - Exécutez les commandes suivantes :
     ```bash
     python -m venv monenv
     ```

3. **Configurer les autorisations d'exécution sur Windows** :

   - Dans PowerShell, tapez :
     ```bash
     Get-ExecutionPolicy
     Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```
   - Choisissez **"Oui pour tout le monde"** si demandé.

4. **Activer l'environnement virtuel** :

   - Exécutez la commande suivante :
     ```bash
     .\monenv\Scripts\Activate
     ```
   - Une fois activé, votre terminal affichera quelque chose comme :
     ```bash
     (monenv)
     ```

### 4. Installer les dépendances  

- Accédez au dossier **Mask_Rcnn** (celui que vous avez cloné depuis GitHub) :  
  ```bash  
  cd Mask_Rcnn  
  ```  
- Installez les dépendances à partir du fichier `requirements.txt` :  
  ```bash  
  pip install -r requirements.txt  
  ```  
- Installez le package :  
  ```bash  
  pip install .  
  ```  
- Une fois l'environnement activé, installez manuellement les dépendances nécessaires si besoin :  
  ```bash  
  pip install tensorflow keras opencv-python numpy matplotlib  
  ```  

---


### 5. Exécution du Projet

- Exécutez le script principal `rcnn.py` : et assurer vous que vous êtes dans l'enivrement virtuelle .
- ![WhatsApp Image 2024-12-17 à 14 29 10_e63babfa](https://github.com/user-attachments/assets/47639c2a-1da7-410a-8e4a-9c2eb04758e2)

  ```bash
  python rcnn.py
  ```

---

## Notes Importantes

- Assurez-vous que le repository **Mask R-CNN** et le fichier **mask\_rcnn\_coco.h5** sont placés correctement.
- Le fichier `rcnn.py` dépend fortement des fichiers de Mask R-CNN pour fonctionner.
- Le projet doit être exécuté dans un environnement Python 3.7.

---

## Liens Utiles

- **Repository Mask R-CNN** : [https://github.com/matterport/Mask\_RCNN](https://github.com/matterport/Mask_RCNN)
- **Modèle Pré-entrainé COCO** : [https://github.com/matterport/Mask\_RCNN/releases](https://github.com/matterport/Mask_RCNN/releases)

---

## Contact

Pour toute question ou assistance, n'hésitez pas à me contacter via GitHub ou par email.
zakariae.khayi@uit.ac.ma

---

Merci d'utiliser **Removing-Undesirable-Objects-MRCNN** !

