# Répertoire Musical – Django

Ce projet est une application web développée avec Django.  
Il permet de répertorier des **groupes de musique** et leurs **albums**, de les consulter, modifier ou supprimer via une interface simple


## Fonctionnalités

- Ajouter / modifier / supprimer des groupes de musique
- Ajouter / modifier / supprimer des albums associés aux groupes renseignés


## Installation

- Télécharger le fichier .zip
- Décompresser l'archive
- Ouvrir le projet dans un environnement virtuel python (pour en créer un : python -m venv .venv)
- Installer django dans la console : pip install django
- Se placer dans le dossier Groupe_album qui est le nom du projet : cd Groupe_musique
- Créer le fichier de migration : python manage.py makemigrations artistes #(artistes étant le nom de l'application)
- Instancier l’ensemble des objets nécessaire à Django pour la base de données : python manage.py migrate
- Enfin démmarer le serveur : python manage.py runserver

Pour se rendre sur le site il suffit de taper cette adresse dans un navigateur : http://127.0.0.1:8000/
Vous serez redirigez vers la page d'acceuil du site (/artistes/index/) qui liste les actions disponibles !


Projet: R2.09 Web dynamique

Auteur : HERCHUEL Lucas - 2025 
