from django.urls import path
from apps.computers.views import ComputerListCreateView, ComputerReadUpdateDeleteView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', ComputerListCreateView.as_view()),
    path('/<int:pk>', ComputerReadUpdateDeleteView.as_view()),
]