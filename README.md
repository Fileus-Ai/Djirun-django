markdown
Copier le code
# Djirun: Django Project Setup CLI

## Introduction

**Djirun** est un outil en ligne de commande conçu pour simplifier le processus de création et de configuration d'un projet Django. Que vous commenciez un nouveau projet ou que vous ayez besoin de configurer diverses fonctionnalités, Djirun facilite la configuration avec des options personnalisables.

## Fonctionnalités

- **Intégration de Framework CSS** : Choisissez entre Bootstrap, Tailwind, ou aucun.
- **Structure des Fichiers Statique** : Option pour créer une structure pour les fichiers statiques.
- **Application à Page Unique** : Configurez facilement une application à page unique.
- **Support de Base de Données** : Utilisez SQLite ou PostgreSQL.
- **Authentification** : Activez l'authentification des utilisateurs dès le départ.
- **API REST** : Intégrez Django REST framework pour construire des APIs.
- **Internationalisation** : Ajoutez un support pour l'internationalisation.
- **Tests Unitaires** : Incluez des tests unitaires de base.
- **Documentation** : Génération automatique d'un fichier README.
- **Support Docker** : Créez une configuration Docker pour la conteneurisation.

## Installation

1. **Clonez le Dépôt** :

   ```bash
   git clone https://github.com/yourusername/djirun.git
   cd djirun
Installez les Dépendances :

Assurez-vous d'avoir Python installé. Créez un environnement virtuel et installez les packages requis :

bash
Copier le code
python -m venv env
source env/bin/activate  # Sur Windows utilisez `env\Scripts\activate`
pip install -r requirements.txt
Installez Click :

Si non inclus dans requirements.txt, installez Click séparément :

bash
Copier le code
pip install click
Utilisation
Vous pouvez utiliser Djirun pour créer et configurer un projet Django depuis la ligne de commande. Voici comment utiliser l'outil CLI :

bash
Copier le code
python cli.py <project_name> [OPTIONS]
Options
--css-framework : Spécifiez le framework CSS à utiliser (options : bootstrap, tailwind, none).
--static-structure / --no-static-structure : Créez une structure pour les fichiers statiques.
--single-page / --no-single-page : Configurez une application à page unique.
--database : Choisissez la base de données (options : sqlite, postgres).
--auth / --no-auth : Activez ou désactivez l'authentification.
--api / --no-api : Activez ou désactivez l'API REST.
--i18n / --no-i18n : Activez ou désactivez l'internationalisation.
--tests / --no-tests : Incluez ou excluez les tests unitaires.
--docs / --no-docs : Générer ou ignorer la documentation.
--docker / --no-docker : Ajouter ou ignorer la configuration Docker.
--python-version : Spécifiez la version de Python pour Docker (ex : 3.8).
Exemple
Pour créer un projet Django nommé myproject avec Bootstrap, une structure de fichiers statiques, l'authentification, et le support Docker :

bash
Copier le code
python cli.py myproject --css-framework bootstrap --static-structure --auth --docker
Tutoriel Détaillé
Étape 1 : Configurez Votre Environnement
Clonez le Dépôt : Téléchargez le projet Djirun sur votre machine locale.

Installez les Dépendances : Configurez un environnement virtuel et installez les packages Python requis.

Étape 2 : Utilisez Djirun pour Créer un Projet Django
Exécutez l'Outil CLI : Utilisez les commandes CLI fournies pour générer votre projet Django avec les configurations désirées.

Détail des Options :

Framework CSS : Choisissez un framework CSS si vous souhaitez styliser votre application.
Structure Statique : Décidez si vous avez besoin d'une structure spécifique pour les fichiers statiques.
Application à Page Unique : Choisissez cette option si votre projet est une application à page unique.
Base de Données : Sélectionnez entre SQLite pour la simplicité ou PostgreSQL pour des performances de production.
Authentification : Activez l'authentification pour gérer les comptes utilisateurs.
API REST : Intégrez le support REST API pour construire des APIs.
Internationalisation : Activez le support pour plusieurs langues.
Tests Unitaires : Ajoutez des tests de base pour vous assurer que votre application fonctionne comme prévu.
Documentation : Générer un fichier README pour votre projet.
Docker : Créez une configuration Docker pour conteneuriser votre application.
Étape 3 : Commencez à Développer
Accédez au Répertoire de Votre Projet : Une fois Djirun terminé la configuration, vous pouvez naviguer dans le répertoire de votre nouveau projet.

Démarrez le Serveur Django : Utilisez le serveur de développement Django pour commencer à construire votre application :

bash
Copier le code
python manage.py runserver
Accédez à Votre Application : Ouvrez votre navigateur web et allez à http://127.0.0.1:8000/ pour voir votre nouveau projet Django en action.

Contribuer
N'hésitez pas à contribuer à Djirun en soumettant des problèmes ou des demandes de tirage. Veuillez suivre les directives de contribution standard de GitHub.

Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour les détails.

bash
Copier le code

Vous pouvez maintenant copier tout le contenu ci-dessus dans un fichier `README.md