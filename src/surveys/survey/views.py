from django.shortcuts import get_object_or_404
from django.db.models import Count, TextField
from django.db.models.functions import Cast
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from survey.models import Survey
from collections.abc import Callable


swagger_stats_response = inline_serializer(
    name="SurveyStatisticsSchema",
    fields={
        "survey_id": serializers.IntegerField(),
        "total_responses": serializers.IntegerField(
            help_text="Всего пройденных опросов"
        ),
        "questions": inline_serializer(
            name="QuestionStatsSchema",
            fields={
                "question_id": serializers.IntegerField(),
                "label": serializers.CharField(),
                "popular_answers": inline_serializer(
                    name="PopularAnswerSchema",
                    fields={
                        "value": serializers.CharField(),
                        "count": serializers.IntegerField(),
                    },
                    many=True,
                ),
            },
            many=True,
        ),
    },
)


@extend_schema(
    summary="Статистика по опросу",
    description="Возвращает количество прохождений и популярные ответы на каждый вопрос.",
    responses={200: swagger_stats_response},
)
@api_view(["GET"])
def get_statistics(_, survey_id: int, get_statistics_port: Callable):
    survey = get_object_or_404(Survey, id=survey_id)
    try:
        result = get_statistics_port(survey)
    except Exception as error:
        return Response({"detail": str(error)}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(result, status=status.HTTP_200_OK)
