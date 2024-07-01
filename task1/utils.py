import requests



def convert_text(text):
    # Convert text to lowercase
    lower_text = text.lower()
    # Replace spaces with +
    formatted_text = lower_text.replace(' ', '+')
    return formatted_text


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_weather_and_location(request):
    # IP geolocation and weather service API keys
    weather_api_key = '01496641e8e04d3c4d8473dba298674b'
    
    # Using IP to fetch location
    ip = get_client_ip(request)
    geo_url = f'https://ipapi.co/102.90.57.253/json/'
    geo_response = requests.get(geo_url).json()
    city = geo_response['city'] or geo_response['country_name']
    converted_city = convert_text(city)
    
    # Using city to fetch weather & temperature
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={converted_city}&appid={weather_api_key}'
    weather_response = requests.get(weather_url).json()
    temperature = weather_response['main']['temp']

    response = {
        'ip': ip,
        'city': city,
        'temperature': temperature
    }
    
    return response