from django.db import transaction
from user_answers.models import UserAnswer

from .desirealizers import CreateData
from .models import SurveyResponse
from survey.models import Survey
from question.models import Question


def create_data_port(data: CreateData):
    survey = Survey.objects.get(id=data.survey_id)
    with transaction.atomic():
        survey_response = SurveyResponse(survey=survey)
        survey_response.save()

        answers = [
            UserAnswer(
                response=survey_response,
                question=Question.objects.get(id=v.question_id),
                value=v.answer.value,
                type=v.answer.type,
            )
            for v in data.answers
        ]
        UserAnswer.objects.bulk_create(answers)
