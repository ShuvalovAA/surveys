from django.db import models

from question.models import Question
from app_types.answer import AnswerType

class Answer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_pos = models.IntegerField(default=0, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=20,
        choices=AnswerType.choices,
        null=False
    )
