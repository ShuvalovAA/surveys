from django.urls import path
from .views import create
from .create_data_port import create_data_port

urlpatterns = [
    path(
        "create",
        create,
        {"create_data_port": create_data_port},
        name="create-survey-response",
    )
]
