from rest_framework import serializers
from .models import Educational
class EducationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educational
        # fields = '__all__'
        fields = ['id', 'title', 'description', 'date','url']
class EducationalHyperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Educational
        fields = ['id', 'title', 'description', 'date', 'url']