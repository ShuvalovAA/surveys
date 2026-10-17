from django.db import models


class AnswerType(models.TextChoices):
    CHECKBOX = 'checkbox', 'чекбокс'
    CUSTOM_TEXT = 'custom_text', 'свой ответ'