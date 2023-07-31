from flask import request
from flask_restx import Resource

from src.application.delivery_app import DeliveryApp


class Delivery(Resource):
    def get(self):
        """Lista todas as entregadas"""
        response = DeliveryApp().get_all()
        return response
