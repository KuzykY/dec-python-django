from django.conf.urls.static import static
from django.urls import include, path

from configs import settings

urlpatterns = [
    path('cars', include('apps.cars.urls')),
    path('auto_parks', include('apps.autopark.urls')),
    path('users', include('apps.users.urls')),
    path('auth', include('apps.auth.urls')),
]
# handler500 = 'rest_framework.exceptions.server_error'
# handler400 = 'rest_framework.exceptions.bad_request'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)