import enum
import json


class Status(enum.Enum):
    OPEN = 1
    CLOSED = 2
    DELETED = 3

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

