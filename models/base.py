import json

from stackOverflow.models.userActivity import UserActivity
from stackOverflow.models.vote import Vote
from stackOverflow.utils import get_current_timestamp, generate_id


class BasePost:

    def __init__(self):
        self._id = generate_id()
        self._title = None
        self._body = None
        self._author = None
        self._createdAt = get_current_timestamp()
        self._editActivity = []
        self._votes = Vote()
        self._tags = []
        self._flag = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def getDict(self):
        try:
            # print(f"inside base: {self}")
            # print(f"inside base: {self.__dict__}")
            dict = self.__dict__.copy()
            votes = self.__dict__['_votes'].__dict__.copy()
            dict['_votes'] = votes
            return dict
        except Exception as e:
            print(f"Something went wrong while getDict in Base Post {str(e)}")

    def upVote(self):
        self._votes.upVote()

    def downVote(self):
        self._votes.downVote()

    def addEditActivity(self, user):
        edit = UserActivity(user)
        self._editActivity.append(edit)

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        self._tags = tags

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def body(self):
        return self._tags

    @body.setter
    def body(self, body):
        self._body = body

    @property
    def flag(self):
        return self._tags

    @flag.setter
    def flag(self, flag):
        self._flag = flag

    @property
    def id(self):
        return self._id

    def editBody(self, user, body):
        self.addEditActivity(user)
        self.body = body

    def editTitle(self, user, title):
        self.addEditActivity(user)
        self.title = title

    def editTags(self, user, tags):
        self.addEditActivity(user)
        self.tags = tags

# b = Base()
#
# b.upVote()
# b.upVote()
# b.upVote()
# b2 = Base()
# print(b.toJSON())
# print(b2.toJSON())
# print(b._votes)
#
# b2 = Base()
# print(b2._votes)
#
# b2._votes.up_vote()
#
#
# print(b._votes)
# print(b2._votes)
