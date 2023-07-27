from flask_restx import Namespace, fields

# Namespaces
user_ns = Namespace('user')

# Payloads
create_payload = user_ns.model('CreatePayload', {
    'name': fields.String(required=True, enum=['valor1', 'valor2', 'valor3']),
    'email': fields.String(required=True)
}, strict=True)

# Headers
