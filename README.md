# Service Web SOAP 

## Introduction
Ce projet implémente un **Service Web SOAP** en utilisant **JAX-WS** en Java. 
L'objectif est d'exposer des opérations simples et de démontrer l'échange de **valeurs primitives** et d'**objets complexes** via le protocole SOAP. Le service est publié localement et peut être testé avec des outils comme **SoapUI**.

## Technologies Utilisées
* **IDE** : IntelliJ IDEA 2025.3.2
* **JDK** JDK : Java 8 (v1.8)
* **Tests**  : SoapUI 5.6.0
* **Frameworks** : JAX-WS & JAXB
* **Protocole** :  SOAP

## Structure du Projet
Le projet est organisé comme suit dans le dossier `src/` :

| Fichier | Description |
| :--- | :--- |
| **Application.java** | Publication du service (Endpoint). |
| **MonserviceWeb.java** | Logique des opérations (Somme, Conversion). |
| **Etudiant.java** | Modèle de données représentant un étudiant. |

## Déploiement du Service
Le service est publié à l'adresse suivante :
`http://localhost:8888/`

Le fichier de description **WSDL** est accessible via :
`http://localhost:8888/?wsdl`

## Description du Web Service
La classe `MonserviceWeb` est exposée en tant que service SOAP avec l'annotation :
`@WebService(targetNamespace = "http://www.polytech.fr")`

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
