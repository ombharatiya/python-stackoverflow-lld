import json

from stackOverflow.models.badge import Badge
from stackOverflow.utils import generate_id


class User:
    def __init__(self, name):
        self._id = generate_id()
        self._name = name
        self._badge = Badge.USER
        self._bounty = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def id(self):
        return self._id

    @property
    def badge(self):
        return self._badge

    @badge.setter
    def badge(self, level):
        self._badge = level

    @property
    def bounty(self):
        return self._badge

    @bounty.setter
    def bounty(self, bounty):
        self._badge = bounty
