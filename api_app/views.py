from rest_framework import status
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DetailSerializer
from main_app.models import Detail

# Create your views here.
@api_view(['GET'])
def documentation(request):
    info = [
        {
            'endpoint': '.../api',
            'method': 'GET',
            'body': None,
            'description': 'View documentation for this API',
        },
        {
            'endpoint': '.../api/post',
            'method': 'POST',
            'body': '{"title": string, "flowrate": float}',
            'description': 'Post flowrate informations',
        },

        'Note: Title field can only be (Patient A) or (Patient B) without blackets'
    ]
    return Response(info, status=status.HTTP_200_OK)

@api_view(['POST'])
def post(request):
    serializer = DetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('SUCCESS', status=status.HTTP_202_ACCEPTED)
    else:
        return Response('FAIL', status=status.HTTP_400_BAD_REQUEST)