from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main_app.models import Customer
from .models import DueSerializer

# Decralation of useful variables
cost_per_unit = 100

# Create your views here.
@api_view(['GET'])
def documentation(request):
    info = [
        {
            'endpoint': '.../api',
            'methode': 'GET',
            'body': None,
            'description': 'View the documentation for this API'
        },{
            'endpoint': '.../api/service',
            'method': 'POST',
            'body': '{"meter_number": str, "units": float}',
            'description': 'Post the unit usage by the specific meternumber'
        }
    ]

    return Response(info, status=status.HTTP_200_OK)

@api_view(['POST'])
def service(request):
    if Customer.objects.filter(meter_number=request.data.get('meter_number')).exists():
        customer = Customer.objects.get(meter_number=request.data.get('meter_number'))

        data = {
            'customer': customer.pk,
            'amount': request.data.get('units') * cost_per_unit,
        }

        serializer = DueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('SUCCESS')
        else:
            return Response('FAIL')
    else:
        return Response('Meter number not exist', status=status.HTTP_404_NOT_FOUND)