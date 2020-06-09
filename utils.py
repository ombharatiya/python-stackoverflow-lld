import json
import uuid
from datetime import datetime


def get_current_timestamp():
    return str(datetime.now())


def generate_id() -> str:
    return str(uuid.uuid4())


def getFormattedData(obj):
    return json.dumps(obj, indent=4)
