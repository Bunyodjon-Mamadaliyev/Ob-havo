from django.urls import path
from .views import ForecastCreateAPIView, ForecastUpdateAPIView, ForecastLocationAPIView

App_name = 'Forecast'

urlpatterns = [
    path('forecasts/', ForecastCreateAPIView.as_view(), name='forecast-create'),
    path('forecasts/<int:pk>/', ForecastUpdateAPIView.as_view(), name='forecast-update'),
    path('forecasts/location/<int:location_id>/', ForecastLocationAPIView.as_view(), name='forecast-by-location'),
]