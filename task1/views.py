from django.http import JsonResponse
from .utils import *


def hello(request):
    visitor = request.GET.get('visitor_name', 'Visitor')
    data = get_weather_and_location(request)
    greeting = f"Hello, {visitor}!, the temperature is {data['temperature']} degrees Celsius in {data['city']}"

    # Response data
    response = {
        'client_ip': data['ip'],
        'location': data['city'],
        'greeting': greeting
    }

    # Return data
    return JsonResponse(response)
