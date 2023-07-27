from flask import request
from flask_restx import Resource

from src.application.delivery_app import DeliveryApp
from src.presentation.payloads.status import delivery_ns, delivery_payload


class Delivery(Resource):
    @delivery_ns.expect(delivery_payload, validate=True)
    def post(self, _id):
        data = request.get_json()

        response = DeliveryApp().change_status(_id, data['new_status'])
        return response
