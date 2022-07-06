from django.urls import path

from .views import AdminToUserView, UserListCreateView, UserToAdminView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>/admin', UserToAdminView.as_view()),
    path('/<int:pk>/not_admin', AdminToUserView.as_view()),
]
