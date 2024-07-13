import json
from app import create_app

app = create_app()
app.testing = True
client = app.test_client()

def test_process_receipt():
    response = client.post('/receipts/process', json={
        "retailer": "Target",
        "purchaseDate": "2023-07-10",
        "purchaseTime": "15:35",
        "items": [
            {"shortDescription": "Item 1", "price": "4.99"},
            {"shortDescription": "Item 2", "price": "0.99"}
        ],
        "total": "5.98"
    })
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "id" in data

def test_get_points():
    response = client.post('/receipts/process', json={
        "retailer": "Target",
        "purchaseDate": "2023-07-10",
        "purchaseTime": "15:35",
        "items": [
            {"shortDescription": "Item 1", "price": "4.99"},
            {"shortDescription": "Item 2", "price": "0.99"}
        ],
        "total": "5.98"
    })
    receipt_id = json.loads(response.data)['id']

    response = client.get(f'/receipts/{receipt_id}/points')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "points" in data
