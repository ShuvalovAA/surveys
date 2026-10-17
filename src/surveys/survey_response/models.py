from django.db import models

from survey.models import Survey

from question.models import Question
from user_answers.models import UserAnswer

class SurveyResponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
