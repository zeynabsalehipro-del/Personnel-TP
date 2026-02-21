from flask import Flask, jsonify, request
app=Flask(__name__)
cards = [
    {"id":1, "name":"Dark Magician", "ATK":2500, "DEF":2100, "Level":8, "Description":"A faire Magicien Sombre"},
]

@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion de carte Yu-Gi-Oh !"

#Endpoint pour lister toutes les cartes
@app.route('/cards', methods=['GET'])
#Méthode HTTP GET qui permet de retourner la liste des étudiants
def get_cards():
    "jsonif transforme la liste de cartes en json"
    return jsonify(cards)

#Ajouter une carte (POST)
@app.route('/cards', methods=['POST'])
def add_element():
    new_card=request.get_json()
    new_card['id']=len(cards)+1
    #Pour récupérer les données envoyé par le client
    cards.append(new_card)
    return jsonify(cards),201
    #Le code 201 pour dire création réussie

#Afficher une carte ayant un identifiant précis
@app.route('/cards/<int:id>', methods=['GET'])
def get_cards_by_id(id):
    card=next((s for s in cards if s['id']==id),None)
    if card:
        return jsonify(card)
    return jsonify({"erreur":"la carte n'existe pas !"}),404

#Afficher une carte ayant un nom précis
@app.route('/cards/<string:name>', methods=['GET'])
def get_cards_by_id(name):
    card=next((s for s in cards if s['name']==name),None)
    if card:
        return jsonify(card)
    return jsonify({"erreur":"la carte n'existe pas !"}),404

#Afficher une carte ayant un niveau précis
@app.route('/cards/level/<int:level>', methods=['GET'])
def get_cards_by_level(level):
    card=next((s for s in cards if s['level']==level),None)
    if card:
        return jsonify(card)
    return jsonify({"erreur":"la carte n'existe pas !"}),404

#Afficher les cartes ayant un niveau inférieur ou égal a celui spécifié
@app.route('/cards/level/less/<int:level>', methods=['GET'])
def get_cards_by_level_less(level):
    lesser_level_cards=[]
    compteur=0
    for s in cards:
        if s['level']<=level:
            lesser_level_cards.append(s)
            compteur=compteur+1
    if compteur>0:
        return jsonify(lesser_level_cards)
    return jsonify({"erreur":"Aucune carte ne correspond !"}),404

#Afficher les cartes ayant un niveau inférieur ou égal a celui spécifié
@app.route('/cards/level/more/<int:level>', methods=['GET'])
def get_cards_by_level_more(level):
    higher_level_cards=[]
    compteur=0
    for s in cards:
        if s['level']>=level:
            higher_level_cards.append(s)
            compteur=compteur+1
    if compteur>0:
        return jsonify(higher_level_cards)
    return jsonify({"erreur":"Aucune carte ne correspond !"}),404

#Mettre a jour une carte PUT
@app.route('/cards/<int:id>', methods=['PUT'])
def update_students(id):
    card=next((s for s in cards if s['id']==id),None)
    if not card:
        return jsonify({"message":"Carte non trouvé !"}),404
    data=request.get_json()
    card.update(data) # Mise a jour des données
    return jsonify(card)

@app.route('/cards/<int:id>', methods=['DELETE'])
def delete_students(id):
    global cards
    cards=[s for s in cards if s['id']!=id]
    return jsonify({"message":"Carte supprimé !"}),200

if __name__=='__main__':
    print("Checkpoint")
    app.run(debug=True)
