from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .models import CarModel
from .serializers import CarSerializer
from core.permissions.user_permissions import IsSuperUser


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        autoParkId = self.request.query_params.get('autoParkId', None)
        if autoParkId:
            return self.queryset.filter(auto_park_id=autoParkId)
        return super().get_queryset()


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)
