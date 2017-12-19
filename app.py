from flask import Flask, jsonify
from flask import request, abort

app = Flask(__name__)

items = [
    {
        'id': 1,
        'name': 'melk',
        'barcode': '25949455',
        'price': 20
    },
    {
        'id': 2,
        'name': 'surlandschips',
        'barcode': '2395329',
        'price': 35
    }
]


@app.route('/handle/api/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})

@app.route('/handle/api/items/barcode=<string:item_barcode>', methods=['GET'])
def get_item_by_barcode(item_barcode):
    item = [item for item in items if item['barcode'] == item_barcode]
    if len(item) == 0:
        abort(404)
    return jsonify({'item': item[0]})


@app.route('/handle/api/items/name=<string:item_name>', methods=['GET'])
def get_item_by_name(item_name):
    item = [item for item in items if item['name'] == item_name]
    if len(item) == 0:
        abort(404)
    return jsonify({'item': item[0]})


@app.route('/handle/api/items/id=<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    item = [item for item in items if item['id'] == item_id]
    if len(item) == 0:
        abort(404)
    return jsonify({'item': item[0]})


@app.route('/handle/api/items/price=<int:item_price>', methods=['GET'])
def get_item_by_price(item_price):
    item = [item for item in items if item['price'] == item_price]
    if len(item) == 0:
        abort(404)
    return jsonify({'item': item[0]})

@app.route('/handle/api/items', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        abort(400)
    item = {
        'id': items[-1]['id']+1,
        'name': request.json['name'],
        'barcode': request.json['barcode'],
        'price': request.json['price']
    }
    items.append(item)
    return jsonify({'item': item}), 201

if __name__ == '__main__':
    app.run(debug=True)


#7038010001321