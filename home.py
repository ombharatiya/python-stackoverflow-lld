from stackOverflow.controllers.appController import AppController
from stackOverflow.utils import getFormattedData

app = AppController.getAppInstance() # A singleton


app.createNewUser("rahul")  # create New User
app.createNewQuestion(None, 'ABC', 'xyz', )  # create New Questions without user E
app.createNewQuestion('rahul', 'ABC', 'xyz', )  # create New Questions with user
app.createNewQuestion('rahul', 'ABC2', 'xysdz', )  # create one more New Questions with user
app.createNewAnswer('rahul', 'ABC', 'myABCanswer')  # create An answer to a Questions with user
app.createNewAnswer('Unknown', 'ABC', 'myABCanswer2')  # create An answer to a Questions without user E
app.createNewComment('rahul', 'ABC', 'my ABC Comment')  # create An answer to a Questions without user
app.createNewComment('Unknown', 'ABC', 'my ABC Comment')  # create An answer to a Questions without user E
q = app.getQuestion('ABC') # get a question
app.upVote(q, 'rahul') # upvote a question with valid user
app.upVote(q, 'kajal') # upvote a question without valid user E
ans_id = app._qa_map['ABC'][0] # get an answer id using one question map
ans = app.getAnswer(ans_id) # get an answer using id
app.downVote(ans, 'rahul') # upvote an answer with valid user
app.upVote(ans, 'kajal') # upvote an answer with valid user E
app.flagPost(ans, 'rahul', "irrelevant") # flag an answer with valid user

# print(app.viewAllQuestions()) # anyone can see all questions
# print(app.viewAllAnswers()) # anyone can see all answers
# print(app.viewAllComments()) # anyone can see all comments
# print(app.viewAllQuestionsAnswersWithComments())  # anyone can see all questions answer with comments
print(getFormattedData(app.viewAllQuestionsAnswersWithComments()))  # anyone can see all questions answer with comments

# print(app.viewQuestion('ABC')) # anyone can see a question

# print(app._questions)
# print(app._answers)
# print(app.__dict__)
