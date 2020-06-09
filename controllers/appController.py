import json

from stackOverflow.customException.customException import CustomException
from stackOverflow.models.answer import Answer
from stackOverflow.models.badge import Badge
from stackOverflow.models.base import BasePost
from stackOverflow.models.comment import Comment
from stackOverflow.models.question import Question
from stackOverflow.models.user import User


class AppController:
    __instance = None
    MODERATOR_POINT = 10

    @staticmethod
    def getAppInstance():
        """ Static access method. """
        if AppController.__instance == None:
            AppController()
        return AppController.__instance

    def __init__(self):
        """ Virtually private constructor. """
        self._questions = {}
        self._answers = {}
        self._comments = {}
        self._users = {}
        self._user_post_map = {}
        self._qa_map = {}
        self._post_comments_map = {}
        if AppController.__instance != None:
            raise Exception("This AppController class is a singleton!")
        else:
            AppController.__instance = self

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__ if type(o) is not 'mappingproxy' else print(f'obj type : {type(o)}'),
    #                       sort_keys=True, indent=4)

    def viewAllQuestions(self):
        try:
            q_list = [i.getDict() for i in self._questions.values()]
            # print('khdckjsanckjsacnkjsacnjsnckjasnckjasnckjqsnc')
            return q_list
        except:
            print("Something went wrong while viewAllQuestions")
        # return list(self._questions.values())

    def viewAllAnswers(self):
        try:
            a_list = [i.__dict__ for i in self._answers.values()]
            return a_list
        except:
            print("Something went wrong while viewAllAnswers")
        # return list(self._questions.values())

    def viewAllComments(self):
        try:
            c_list = [i.__dict__ for i in self._comments.values()]
            return c_list
        except:
            print("Something went wrong while viewAllComments")
        # return list(self._questions.values())

    def viewAllQuestionsAnswersWithComments(self):
        try:
            qa = []
            for q_key, q_val in self._questions.items():
                item = {
                    "question": q_val.getDict(),
                    "comments": self.viewAllCommentsOfPost(q_key)
                }
                answers = {}
                if q_key in self._qa_map:
                    ans_list = self._qa_map[q_key]
                    for ans_id in ans_list:
                        if ans_id in self._answers:
                            answers.update({ans_id: {
                                "answer": self._answers[ans_id].getDict(),
                                "comments": self.viewAllCommentsOfPost(ans_id)
                            }})
                item.update({
                    "answers": answers
                })
                qa.append(item)

            return qa
        except:
            print("Something went wrong while viewAllQuestionsAnswers")
        # return list(self._questions.values())

    def viewAllCommentsOfPost(self, post_id):
        try:
            comments = []
            if post_id in self._post_comments_map:
                comments_list = self._post_comments_map[post_id]
                for comment_id in comments_list:
                    if comment_id in self._comments:
                        comments.append(self._comments[comment_id].getDict())
            return comments
        except:
            print("Something went wrong while viewAllQuestionsAnswers")

    def viewQuestion(self, id):
        if id in self._questions:
            # return self._questions[id]
            return self._questions[id].getDict()
        else:
            raise CustomException("Question not found")

    def viewAnswer(self, id):
        if id in self._answers:
            # return self._questions[id]
            return self._answers[id].getDict()
        else:
            raise CustomException("Answer not found")

    def getQuestion(self, id):
        if id in self._questions:
            return self._questions[id]
        else:
            raise CustomException("Question not found")

    def getAnswer(self, id):
        if id in self._answers:
            return self._answers[id]
        else:
            raise CustomException("Answer not found")

    def createNewUser(self, name=None):
        try:
            if name is None:
                raise CustomException("User's name cannot be none or null")

            user = User(name)
            self._users.update({user.name: user})
            # self._users.update({user.id: user})
            return user
        except CustomException as error:
            print(f'A New Exception occurred: {error.value}')
        except Exception as e:
            print(f"Error Occurred while Creating New User: {str(e)}")

    def createNewQuestion(self, user=None, title=None, body=None, tags=None, bounty=None):

        try:
            if user is None or user not in self._users:
                raise CustomException("You must be User to create a question")

            question = Question.create(user, title, body)

            if bounty:
                question.bounty = bounty

            if tags is not None and tags != []:
                question.tags = tags
            # print(question.__dict__)
            self._questions.update({question._title: question})

            # Adding post to user post map
            self.add_to_user_post_map(user, question._title)

            # self._questions.update({question.id: question})
            return question

        except CustomException as error:
            print(f'A New Exception occurred: {error.value}')
        except Exception as e:
            print(f"Error Occurred while Creating New Question: {str(e)}")

    def createNewAnswer(self, user=None, question=None, body=None):
        try:
            if user is None or user not in self._users:
                raise CustomException("You must be User to create an Answer")

            if question is None or question not in self._questions:
                raise CustomException("Question Invalid")

            if body is None or body == '':
                raise (CustomException("Answer body cannot be empty or null"))

            answer = Answer.create(user, question, body)
            question_obj = self._questions[question]
            if question_obj.hasBounty():
                answer.bounty = question_obj.bounty

            self.add_to_qa_map(question, answer._id)
            self.add_to_user_post_map(user, answer._id)

            self._answers.update({answer.id: answer})
            return answer

        except CustomException as error:
            print(f'A New Exception occurred: {error.value}')
        except Exception as e:
            print(f"Error Occurred while Creating New Answer: {str(e)}")

    def createNewComment(self, user=None, post=None, body=None):
        try:
            if user is None or user not in self._users:
                raise CustomException("You must be a User to add a comment")

            if post is None or (post not in self._questions and post not in self._answers):
                print(post)
                raise CustomException("Post Invalid")

            if body is None or body == '':
                raise (CustomException("comment body cannot be empty or null"))

            comment = Comment.create(user, post, body)

            self.add_to_post_comments_map(post, comment._id)
            self.add_to_user_post_map(user, comment._id)

            self._comments.update({comment.id: comment})
            return comment

        except CustomException as error:
            print(f'A New Exception occurred: {error.value}')
        except Exception as e:
            print(f"Error Occurred while Creating New comment: {str(e)}")

    def add_to_user_post_map(self, user, post):
        try:
            all_posts_of_user = self._user_post_map[user] if user in self._user_post_map else []
            all_posts_of_user.append(post)
            self._user_post_map.update({user: all_posts_of_user})
        except Exception as e:
            print(f"Error Occurred while add_to_user_post_map: {str(e)}")

    def add_to_qa_map(self, question, answer):
        try:
            all_a_of_q = self._qa_map[question] if question in self._qa_map else []
            all_a_of_q.append(answer)
            self._qa_map.update({question: all_a_of_q})
        except Exception as e:
            print(f"Error Occurred while add_to_qa_map: {str(e)}")

    def add_to_post_comments_map(self, post, comment):
        try:
            all_comm_of_post = self._post_comments_map[post] if post in self._post_comments_map else []
            all_comm_of_post.append(comment)
            self._post_comments_map.update({post: all_comm_of_post})
        except Exception as e:
            print(f"Error Occurred while add_to_post_comments_map: {str(e)}")

    def add_bounty_to_user(self, user, bounty):
        user_obj = self._users[user]
        user_bounty = user_obj.bounty
        if bounty > 0:
            user_obj.bounty = user_bounty + bounty

        self.checkUserPromotion(user)

    def checkUserPromotion(self, user):
        try:
            user_obj = self._users[user]
            user_bounty = user_obj.bounty
            if user_bounty > self.MODERATOR_POINT:
                user_obj.badge = Badge.MODERATOR
        except Exception as e:
            print(f"Error Occurred while checking User Promotion: {str(e)}")

    def upVote(self, obj: BasePost, user):
        try:
            if user is None or user not in self._users:
                raise CustomException("You must be User to make a Vote")
            obj.upVote()
        except CustomException as error:
            print(f'A New Exception occurred: {error.value}')
        except Exception as e:
            print(f'Something Went Wrong while upVote: {str(e)}')

    def downVote(self, obj: BasePost, user):
        try:
            if user is None or user not in self._users:
                raise CustomException("You must be User to make a Vote")
            obj.downVote()
        except CustomException as error:
            print(f'A New Exception occurred: {error.value}')
        except Exception as e:
            print(f"Something Went Wrong while upVote: {str(e)}")

    def flagPost(self, obj: BasePost, user, message):
        try:
            if user is None or user not in self._users:
                raise CustomException("You must be User to flag a Post")
            if message is None or message == '':
                raise CustomException("message must not be null or empty")
            obj.flag = message
        except CustomException as error:
            print(f'A New Exception occurred: {error.value}')
        except Exception as e:
            print(f'Something Went Wrong while upVote: {str(e)}')

# v = AppController()
#
# print(v)
# v2 = AppController.getInstance()
# print(v2.up_AppController())
# print(v2.up_AppController())
# print(v2.up_AppController())

# print(v)
# print(v2)
