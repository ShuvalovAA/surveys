from django.contrib.auth.models import User
from django.db import models

from question.models import Question
from app_types.answer import AnswerType

class UserAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    response = models.ForeignKey(
        'survey_response.SurveyResponse',
        on_delete=models.CASCADE,
        related_name='answers'
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.JSONField(null=True)
    type = models.CharField(max_length=20, choices=AnswerType.choices, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
