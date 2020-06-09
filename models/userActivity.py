import json

from stackOverflow.utils import get_current_timestamp, generate_id


class UserActivity:
    def __init__(self, actor):
        self._id = generate_id()
        self._timestamp = get_current_timestamp()
        self._actor = actor

        def toJSON(self):
            return json.dumps(self, default=lambda o: o.__dict__,
                              sort_keys=True, indent=4)

