from django.urls import path
from .views import get_statistics
from .ports.get_statistics_port import get_statistics_port


urlpatterns = [
    path(
        "<int:survey_id>/statistics/",
        get_statistics,
        {'get_statistics_port': get_statistics_port},
        name="survey-statistics"
    )
]