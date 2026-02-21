from flask import Flask, jsonify, request
app=Flask(__name__)
cards = [
    { "id": 1,"name":"Dark Magician","ATK": 2500,"DEF": 2100, "Level": 8,"Description": "A faire Magicien Sombre"},
    {"id": 2,"name": "Blue-Eyes White Dragon","ATK": 3000,"DEF": 2500,"Level": 8,"Description": "A faire Dragon Blanc aux Yeux Bleus"}
]

@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion de carte !"

@app.route('/cards', methods=['GET'])
def get_cards():
    return jsonify(cards)

@app.route('/cards', methods=['POST'])
def add_element():
    new_card = request.get_json()
    new_card['id'] = len(cards) + 1
    cards.append(new_card)
    return jsonify(cards), 201

@app.route('/cards/<int:id>', methods=['GET'])
def get_cards_by_id(id):
    card = next((s for s in cards if s['id'] == id), None)
    if card:
        return jsonify(card)
    return jsonify({"erreur": "la carte n'existe pas !"}), 404

@app.route('/cards/name/<string:name>', methods=['GET'])
def get_cards_by_name(name):
    card = next((s for s in cards if s['name'] == name), None)
    if card:
        return jsonify(card)
    return jsonify({"erreur": "la carte n'existe pas !"}), 404

@app.route('/cards/<int:id>', methods=['PUT'])
def update_cards(id):
    card = next((s for s in cards if s['id'] == id), None)
    if not card:
        return jsonify({"message": "Carte non trouvé !"}), 404
    data = request.get_json()
    card.update(data)
    return jsonify(card)

@app.route('/cards/<int:id>', methods=['DELETE'])
def delete_cards(id):
    global cards
    cards = [s for s in cards if s['id'] != id]
    return jsonify({"message": "Carte supprimé !"}), 200

if __name__ == '__main__':
    print("Server Yu-Gi-Oh is starting on port 5000...")
    app.run(debug=True)
