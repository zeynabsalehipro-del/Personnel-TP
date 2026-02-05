# Service Web SOAP 

## Introduction
'L'objectif principal de ce travail pratique est le **développement d'un service web** en utilisant Java. Ce projet vise à approfondir la compréhension du fonctionnement des services web, notamment leur description via le fichier **WSDL** et les mécanismes de communication entre un client et le serveur.'

## Description Technique
Ce travail pratique implémente un **Service Web SOAP** en utilisant **JAX-WS** en Java. L'objectif est d'exposer des opérations simples et de démontrer l'échange de **valeurs primitives** ainsi que d'**objets complexes** via le protocole SOAP.

### Pourquoi SOAP ?
Le protocole **SOAP** (Simple Object Access Protocol) permet à des applications hétérogènes de communiquer entre elles via le réseau. Dans ce projet :
* **Format des données :** Les échanges sont structurés en **XML**.
* **Protocole de transport :** Les messages sont transmis via **HTTP**.
* **Accès :** Une fois déployé, le service est accessible via une **URL** spécifique et peut être testé avec des outils comme **SoapUI** ou **Postman**.

## Technologies Utilisées
* **IntelliJ** 
* **Postman**
* **Java** 
* **SoapUI**
* packages :
  * `JAX-WS (Java API for XML Web Services)`
  * `JAXB (for XML object mapping)`

## Structure du Projet
Le projet est organisé comme suit dans le dossier `src/` :

| Fichier | Description |
| :--- | :--- |
| **Application.java** | Classe principale pour publier le service SOAP. |
| **MonserviceWeb.java** | Définit les opérations et la logique du service. |
| **Etudiant.java** | Modèle de données représentant un étudiant. |

## Déploiement du Service
Le service est publié à l'adresse suivante :
`http://localhost:8888/`

Le fichier de description **WSDL** est accessible via :
`http://localhost:8888/?wsdl`

## Description du Web Service
La classe `MonserviceWeb` est exposée en tant que service SOAP avec l'annotation :
`@WebService`

### Opérations disponibles :
* **`convertir`** : Convertit une valeur numérique (multiplication par 0.9).
* **`somme`** : Calcule la somme de deux nombres décimaux.
* **`getEtudiant`** : Retourne un objet `Etudiant` en fonction d'un identifiant.

## Modèle de Données (Classe Etudiant)
La classe `Etudiant` représente un **type SOAP complexe**. Elle utilise l'annotation `@XmlRootElement` pour la sérialisation.

**Attributs :**
* `identifiant` (int)
* `nom` (String)
* `moyenne` (double)


