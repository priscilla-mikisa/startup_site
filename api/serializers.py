from rest_framework import serializers
from submissions.models import StartupSubmission

class StartupSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupSubmission
        fields = '__all__'
