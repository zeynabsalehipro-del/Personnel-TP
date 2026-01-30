# SAE — Développement & Déploiement d'une Application Web RESTful Conteneurisée

## 1. Contexte du projet
Ce projet a été réalisé dans le cadre de la SAE. Il consiste à concevoir et déployer une application web complète disposant d'un backend exposant une **API RESTful**. L'objectif principal est de maîtriser le cycle de vie logiciel, de la programmation orientée services jusqu'à l'utilisation des outils **DevOps** comme Docker.

## 2. Architecture du projet
L'application repose sur une architecture modulaire :
* **Backend** : Développé avec [Indiquez votre langage/framework, ex: Java Spring Boot ou Python FastAPI].
* **Base de données** : Relationnelle ([Indiquez ex: PostgreSQL ou MySQL]) avec une persistance gérée via un **ORM**.
* **Conteneurisation** : L'ensemble est orchestré via **Docker Compose** pour assurer la portabilité.

### Modélisation des données
Nous avons implémenté les relations suivantes dans notre base de données :
* One-to-One
* One-to-Many / Many-to-One
* Many-to-Many

## 3. Routes de l'API REST
Voici quelques exemples de routes disponibles :
* `GET /api/v1/[nom_ressource]` : Récupérer la liste des éléments.
* `POST /api/v1/[nom_ressource]` : Créer un nouvel élément.
* `PUT /api/v1/[nom_ressource]/{id}` : Mettre à jour un élément existant.
* `DELETE /api/v1/[nom_ressource]/{id}` : Supprimer un élément.

## 4. Lancement de l'application
Pour lancer l'application en local avec Docker Compose, exécutez la commande suivante à la racine du projet :

```bash
docker-compose up --build
