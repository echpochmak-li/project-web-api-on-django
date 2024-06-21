from rest_framework import serializers
from .models import *

#делаем данные в json 

class SerialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serials
        fields = '__all__'