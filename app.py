from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': "My First Store",
        'items': [
            {
                'name': "first item",
                'price': 10.99
            }
        ]
    }
]


@app.route('/')
def home():
    return render_template('index.html')


# POST - /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    dictionary = {'name': request_data['name'],
                  'items': []
                  }
    stores.append(dictionary)
    return jsonify(dictionary)


# GET - /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)
    return jsonify({"error": "no such store exist"})


# GET - /store
@app.route('/store', methods=['GET'])
def get_all_stores():
    return jsonify({'stores': stores})


# POST - /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['GET'])
def create_store_item():
    pass


# GET - /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_store_item():
    pass


app.run(port=5000)
