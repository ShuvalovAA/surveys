
from django.db.models import Count, TextField
from django.db.models.functions import Cast

from user_answers.models import UserAnswer
from survey_response.models import SurveyResponse


def get_statistics_port(survey):
    total_responses = SurveyResponse.objects.filter(survey=survey).count()

    stats_query = (
        UserAnswer.objects.filter(response__survey=survey)
        .annotate(value_text=Cast("value", output_field=TextField()))
        .values("question_id", "question__label", "value_text")
        .annotate(count=Count("id"))
        .order_by("question_id", "-count")
    )

    questions_dict = {}
    for row in stats_query:
        q_id = row["question_id"]

        if q_id not in questions_dict:
            questions_dict[q_id] = {
                "question_id": q_id,
                "label": row["question__label"],
                "popular_answers": [],
            }

        questions_dict[q_id]["popular_answers"].append(
            {"value": row["value_text"], "count": row["count"]}
        )

    return {
        "survey_id": survey.id,
        "total_responses": total_responses,
        "questions": list(questions_dict.values()),
    }
