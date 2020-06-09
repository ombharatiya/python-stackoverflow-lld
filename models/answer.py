from stackOverflow.customException.customException import CustomException
from stackOverflow.models.base import BasePost


class Answer(BasePost):

    def __init__(self, user, question, body):
        """

        :rtype: Question
        :param user:
        :param title:
        :param body:
        """
        super().__init__()
        self._deleted = False
        self._question = question
        self._author = user
        self._body = body
        self._bounty = 0

    @staticmethod
    def create(user, question, body, **kwargs):
        if user is None:
            raise (CustomException("User cannot be empty or null"))

        if question is None:
            raise CustomException("Question Invalid")

        if body is None or body == '':
            raise (CustomException("Question body cannot be empty or null"))

        return Answer(user, question, body)

    @property
    def bounty(self):
        return self._badge

    @bounty.setter
    def bounty(self, bounty):
        self._badge = bounty
