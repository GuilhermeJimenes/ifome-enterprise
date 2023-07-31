from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from src.presentation.payloads.delivery import delivery_ns
from src.presentation.resources.delivery import Delivery

print('public')

# configs
app = Flask(__name__)
cors = CORS(app)
api = Api(app)

# namespaces
api.add_namespace(delivery_ns)

# resources
delivery_ns.add_resource(Delivery, '')
