from flask import Flask
from .routes import receipt_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(receipt_blueprint)
    return app
