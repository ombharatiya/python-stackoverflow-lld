from stackOverflow.customException.customException import CustomException
from stackOverflow.models.base import BasePost
from stackOverflow.models.status import Status


class Question(BasePost):

    def __init__(self, user, title, body):
        """

        :rtype: Question
        :param user:
        :param title:
        :param body:
        """
        super().__init__()
        self._status = Status.OPEN
        self._author = user
        self._title = title
        self._body = body
        self._bounty = 0

    @staticmethod
    def create(user, title, body, **kwargs):
        if user is None:
            raise (CustomException("User cannot be empty or null"))

        if title is None or title == '':
            raise (CustomException("Title cannot be empty or null"))

        if body is None or body == '':
            raise (CustomException("Question body cannot be empty or null"))

        question = Question(user, title, body)

        if 'tags' in kwargs:
            question.tags = kwargs['tags']

        if 'bounty' in kwargs:
            question.bounty = kwargs['bounty']

        return question

    def getDict(self):

        try:
            dict = super().getDict().copy()
            status = super().getDict()['_status'].name
            dict['_status'] = status
            return dict
        except Exception as e:
            print(f"Something went wrong while getDict in Question {str(e)}")

    @property
    def bounty(self):
        return self._badge

    @bounty.setter
    def bounty(self, bounty):
        self._badge = bounty

    def hasBounty(self):
        return self._bounty > 0

    @property
    def status(self):
        return self._badge

    @status.setter
    def status(self, status):
        if type(status) == Status:
            self._status = status
