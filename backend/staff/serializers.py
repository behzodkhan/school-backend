from rest_framework.serializers import ModelSerializer
from .models import *

class StaffSerializers(ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'