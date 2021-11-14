from .models import PrioritySubmission
from rest_framework import serializers


class PrioritySubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrioritySubmission
        fields = '__all__'
