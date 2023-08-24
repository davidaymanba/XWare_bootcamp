from rest_framework import serializers
from .models import visitor



class VisitorsSerializers(serializers.ModelSerializer):
        class Meta:
             model = visitor
             fields = '__all__'