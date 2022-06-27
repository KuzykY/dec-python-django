from rest_framework.serializers import ModelSerializer
from .models import ComputerModel

class ComputerSerializer(ModelSerializer):
    class Meta:
        model=ComputerModel
        # fields='__all__'
        fields=('id','brand','model','ram','monitor_inches')
