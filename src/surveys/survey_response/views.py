from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_types.answer import AnswerType
from .desirealizers import deserialize_data
swagger_request_schema = inline_serializer(
    name='CreateDataSchema',
    fields={
        'survey': serializers.IntegerField(help_text='ID опроса'),
        'answers': inline_serializer(
            name='AnswerDataSchema',
            fields={
                'question': serializers.IntegerField(help_text='ID вопроса'),
                'value': serializers.CharField(),
                'type': serializers.ChoiceField(choices=AnswerType.values)
            },
            many=True #
        )
    }
)
@extend_schema(
    summary='Создать ответ на опрос',
    description='Принимает ID опроса и массив ответов на вопросы.',
    request=swagger_request_schema,
    responses={201: {'ok': 'ok'}},
)
@api_view(['POST'])
def create(request, create_data_port):

    try:
        data= deserialize_data(request.data)
    except TypeError as error:
        return Response({'detail': str(error)}, status.HTTP_400_BAD_REQUEST)
    except ValueError as error:
        return Response({'detail': str(error)}, status.HTTP_400_BAD_REQUEST)


    try:
        create_data_port(data)
    except Exception as error:
        return Response({'detail': str(error)}, status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'detail': request.data}, status.HTTP_201_CREATED)
