from django.db import models

from survey.models import Survey


class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    label = models.CharField(max_length=255, verbose_name='Текст вопроса', null=False)
    order_pos = models.IntegerField(default=0, null=False)
