import json
from decimal import Decimal

#Decimal cannot be directly converted to JSON, therefore a custom encoder is necessary
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(DecimalEncoder, self).default(obj)
