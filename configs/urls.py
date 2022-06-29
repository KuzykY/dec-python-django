from django.urls import path, include

urlpatterns = [
    path('cars', include('apps.cars.urls')),
    path('auto_parks', include('apps.autopark.urls'))
]
