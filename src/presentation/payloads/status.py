from flask_restx import Namespace, fields

from src.domain.constants import DELIVERY_STATUS

# Namespaces
delivery_ns = Namespace('delivery')

# Payloads
delivery_payload = delivery_ns.model('DeliveryPayload', {
    'new_status': fields.String(required=True, enum=DELIVERY_STATUS)
}, strict=True)

# Headers
