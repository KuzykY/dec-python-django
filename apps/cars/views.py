from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import CarSerializer
from .models import CarModel


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_queryset(self):
        autoParkId = self.request.query_params.get('autoParkId', None)
        if autoParkId:
            return self.queryset.filter(auto_park_id=autoParkId)
        return super().get_queryset()


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
