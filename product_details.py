from flask import Flask, jsonify

app = Flask(__name__)

# Sample product details data
products = {
    "1": {"id": "1", "name": "Honey Lemon", "category": "Beverages", "price": "$3.50", "description": "Fresh and sweet honey lemon drink."},
    "2": {"id": "2", "name": "Lemon Salad", "category": "Salads", "price": "$5.00", "description": "Crisp salad with a tangy lemon dressing."},
    "3": {"id": "3", "name": "Lemon Dessert", "category": "Desserts", "price": "$4.00", "description": "Sweet dessert infused with natural lemon flavor."}
}

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(list(products.values()))

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
