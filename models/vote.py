import json


class Vote:
    def __init__(self):
        """ Virtually private constructor.
        :rtype: Vote
        """
        self._up = 0
        self._down = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __str__(self):
        return F'votes up: {self._up}, down: {self._down}'

    def upVote(self):
        self._up = self._up + 1
        return self._up

    def downVote(self):
        self._down = self._down + 1
        return self._down

    def getUpVotes(self):
        return self._up

    def getDownVotes(self):
        return self._down

# v = Vote()
#
# print(v)
# v2 = Vote()
# print(v2.up_vote())
# print(v2.up_vote())
# print(v2.up_vote())
#
# print(v)
# print(v2)
