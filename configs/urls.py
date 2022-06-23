from django.contrib import admin
from django.urls import path

from userlist.views import UsersListCreateView, UserByIdView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('users', UsersListCreateView.as_view()),
    path('users/<int:pk>', UserByIdView.as_view()),
]
