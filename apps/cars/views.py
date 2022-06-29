from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import CarSerializer
from .models import CarModel


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_queryset(self):
        autoParkId = self.request.query_params.get('autoParkId')
        if autoParkId:
            return self.queryset.filter(autoParkId=autoParkId)
        return super().get_queryset()

    # def get_queryset(self):
    #     autoParkId = self.request.query_params.get('autoParkId')
    #     if autoParkId:
    #         return self.queryset.filter(autoParkId=autoParkId)
    #     return super().get_queryset()


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
