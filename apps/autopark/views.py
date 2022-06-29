from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveDestroyAPIView

from .models import AutoParkModel
from .serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkAddCarView(CreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)
