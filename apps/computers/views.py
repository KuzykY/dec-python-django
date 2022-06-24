from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ComputerModel

class ComputerListCreateView(APIView):
    def post(self,*args,**kwargs):
        data = self.request.data
