import enum
import json


class Badge(enum.Enum):
    USER = 1
    MODERATOR = 2

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

