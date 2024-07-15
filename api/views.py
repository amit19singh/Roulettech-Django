from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class CurrentWeatherView(APIView):
    def get(self, request, city, format=None):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        return Response(response.json())
    
    
class WeatherForecastView(APIView):
    def get(self, request, city, format=None):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
        response = requests.get(url)
        return Response(response.json())



class CitySearchView(APIView):
    def get(self, request, format=None):
        query = request.query_params.get('query', '')
        cities = [{'name': 'New York'}, 
                  {'name': 'Los Angeles'}, 
                  {'name': 'Chicago'}, 
                  {'name': 'Bloomington'}, 
                  {'name': 'Ohio'}]
        if query:
            filtered_cities = [city for city in cities if query.lower() in city['name'].lower()]
        else:
            filtered_cities = cities
        return Response(filtered_cities)



