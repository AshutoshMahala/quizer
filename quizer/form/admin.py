from django.contrib import admin
from .models import User, Question, Quiz, Response

# Register your models here.

admin.site.register(User)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Response)