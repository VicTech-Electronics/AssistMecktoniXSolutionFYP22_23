from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from main.models import Customer


# Create your views here.
@api_view(['GET'])
def documentation(request):
    pass
    info = [
        {
            'endpoint': '.../api',
            'method': 'GET',
            'body': None,
            'description': 'View documentation for this API'
        },
        {
            'endpoint': '.../api/usage',
            'methode': 'POST',
            'body': '{"meter_number": str, "units": float}',
            'response': '{"units": float,"status": boolean}',
            'description': 'Update units used'
        },
        {
            'endpoint': '.../api/topup',
            'methode': 'POST',
            'body': '{"meter_number": str, "units": float}',
            'response': '{"units": float,"status": boolean}',
            'description': 'Update meter topup units'
        }
    ]
    return Response(info, status=status.HTTP_200_OK)

@api_view(['POST'])
def usage(request):
    meter_number = request.data.get('meter_number')
    if Customer.objects.filter(meter_number = meter_number).exists():
        customer = Customer.objects.get(meter_number = meter_number)
        remaining_units = customer.units - request.data.get('units')

        if remaining_units < 0.0:
            remaining_units = 0.0
        
        customer.units = remaining_units
        customer.save()

        payload = {
            'units': remaining_units,
            'status': customer.status
        }
        return Response(payload)
    else:
        return Response(f'Customer of meter number {meter_number}, Not exist')
    


@api_view(['POST'])
def meterTopup(request):
    meter_number = request.data.get('meter_number')
    if Customer.objects.filter(meter_number = meter_number).exists():
        customer = Customer.objects.get(meter_number = meter_number)
        remaining_units = customer.units + request.data.get('units')

        if remaining_units < 0.0:
            remaining_units = 0.0
        
        customer.units = remaining_units
        customer.save()

        payload = {
            'units': remaining_units,
            'status': customer.status
        }
        return Response(payload)
    else:
        return Response(f'Customer of meter number {meter_number}, Not exist')
    