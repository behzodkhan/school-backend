from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def index(request):
    staff = Staff.objects.all()
    serializer = StaffSerializers(staff, many=True)
    return Response(serializer.data)