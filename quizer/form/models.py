from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    created_at = models.DateTimeField('time created', auto_now_add=True)


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100)
    created_at = models.DateTimeField('time published', auto_now_add=True)
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_questions = models.IntegerField(default=5)

    def to_dict(self):
        return {
            'quiz_name': self.quiz_name,
            'num_questions': self.num_questions,
            'quiz_id': self.id
        }


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created_at = models.DateTimeField('time created', auto_now_add=True)

    def __str__(self):
        return self.question_text


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    created_at = models.DateTimeField('time of response', auto_now_add=True)

    def __str__(self):
        return self.answer