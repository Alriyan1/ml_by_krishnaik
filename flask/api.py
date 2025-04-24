from flask import Flask, request, jsonify

app = Flask(__name__)

items =[
    { 'id': 1, 'name': 'item1', 'description': 'This is item 1' },
    { 'id': 2, 'name': 'item2', 'description': 'This is item 2' },
]

@app.route('/')
def home():
    return 'Welcome to the Sample TODO list app'

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item == None:
        return jsonify({ 'message': 'Item not found' })

    return jsonify(item)

@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({ 'message': 'Item name is required' })
    new_item={
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item == None:
        return jsonify({ 'message': 'Item not found' })
    
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])

    return jsonify(item)


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    
    return jsonify({ 'results': 'item deleted' })


if __name__ == '__main__':
    app.run(debug=True)