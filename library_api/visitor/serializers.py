from rest_framework import serializers
from .models import visitor



class visitors_serializers(serializers.ModelSerializer):
        class Meta:
             model = visitor
             fields = '__all__'