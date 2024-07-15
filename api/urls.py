from django.urls import path
from .views import CurrentWeatherView, WeatherForecastView, CitySearchView

urlpatterns = [
    path('weather/current/<str:city>/', CurrentWeatherView.as_view(), name='current-weather'),
    path('weather/forecast/<str:city>/', WeatherForecastView.as_view(), name='weather-forecast'),
    path('city/search/', CitySearchView.as_view(), name='city-search'),
]

