from ninja import NinjaAPI
import json

from . import services
from .schemas import QuizIn, QuestionsIn, QuestionOut, UserOut, QuestionDto

api = NinjaAPI()


@api.post("create-quiz/", response={200: int})
def create_quiz(request, data: QuizIn):
    quiz = services.create_quiz(data)
    return quiz.id


@api.post("create-question/", response={200: None})
def create_questions(request, data: QuestionsIn):
    services.create_question(data)


@api.get("quiz/{quiz_id}")
def get_questions(request, quiz_id: int):
    questions_list = services.get_questions(quiz_id)
    result = []
    for question in questions_list:
        result.append({"question_id": question.id, "question_text": question.question_text})

    return result

@api.get("users", response={200: list[UserOut]})
def get_users(request):
    return services.get_all_users()

@api.get("quizes")
def get_quizes(request):
    result = []
    for quiz in services.get_all_quizes():
        result.append({"id": quiz.id, "name": quiz.quiz_name, 'num_questions': quiz.num_questions})
    return result