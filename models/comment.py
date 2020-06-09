from stackOverflow.customException.customException import CustomException
from stackOverflow.models.base import BasePost


class Comment(BasePost):

    def __init__(self, user, post, body):
        """

        :rtype: Comment
        :param user:
        :param post:
        :param body:
        """
        super().__init__()
        self._author = user
        self._post = post
        self._body = body

    @staticmethod
    def create(user, post, body, **kwargs):
        if user is None:
            raise (CustomException("User cannot be empty or null"))

        if post is None:
            raise (CustomException("Post cannot be empty or null"))

        if body is None or body == '':
            raise (CustomException("Question body cannot be empty or null"))

        return Comment(user, post, body)


