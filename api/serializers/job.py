from rest_framework import serializers
from api.models import Job


class JobSerializer(serializers.ModelSerializer):
    detail_url = serializers.URLField(source='get_absolute_url',read_only=True)
    class Meta:
        model = Job
        fields = '__all__'