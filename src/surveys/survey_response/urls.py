from django.urls import path, include
from .views import create
from functools import partial
from .create_data_port import create_data_port


urlpatterns = [
    path(
        "create",
        partial(
            create,
            create_data_port=create_data_port
        ),
        name='create-survey-response'
    ),
]
