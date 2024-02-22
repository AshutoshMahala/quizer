from .models import Quiz, User, Question, Response


def create_quiz(quiz_data):
    user = User.objects.get(user_name=quiz_data.user_name)
    quiz = Quiz.objects.create(quiz_name=quiz_data.user_name, admin_user=user, num_questions=5)
    quiz.save()
    return quiz


def create_question(question_data):
    try:
        quiz = Quiz.objects.get(id=question_data.quiz_id)
    except Quiz.DoesNotExist:
        # throw "No such quiz
        raise Http404("Quiz not found")
    for question_statement in question_data.questions:
        question = Question.objects.create(question_text=question_statement, quiz=quiz)
        question.save()


def get_questions(quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    return list(Question.objects.filter(quiz=quiz))


def get_all_quizes():
    return list(Quiz.objects.all())


def create_response(user_name, question_id, response_text):
    Response.objects.create(user_name=user_name, question_id=question_id, repsonse_text=response_text)


def get_all_users():
    return list(User.objects.all())
