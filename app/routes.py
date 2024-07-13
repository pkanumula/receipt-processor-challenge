from flask import Blueprint, request, jsonify
from .models import Receipt

receipt_blueprint = Blueprint('receipt', __name__)

receipts = {}

@receipt_blueprint.route('/receipts/process', methods=['POST'])
def process_receipt():
    data = request.json
    receipt = Receipt(
        retailer=data['retailer'],
        purchase_date=data['purchaseDate'],
        purchase_time=data['purchaseTime'],
        items=data['items'],
        total=data['total']
    )
    receipts[receipt.id] = receipt
    return jsonify({"id": receipt.id}), 200

@receipt_blueprint.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):
    receipt = receipts.get(id)
    if receipt is None:
        return jsonify({"error": "Receipt not found"}), 404
    return jsonify({"points": receipt.points}), 200
