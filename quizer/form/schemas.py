from ninja import Schema


class QuizIn(Schema):
    quiz_name: str
    user_name: str
    num_questions: int = 5

class QuestionsIn(Schema):
    questions: list[str]
    quiz_id: int


class QuestionOut(Schema):
    question_id: int
    question_text: str


class QuestionDto:
    def __init__(self):
        self.quiz_id = -1
        self.quiz_name = None

    def to_dict(self):
        return {
            'quiz_id': self.quiz_id,
            'quiz_name': self.quiz_name,
        }


class UserOut(Schema):
    user_name: str
    id: int
    user_email: str = None
