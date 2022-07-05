from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer


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
