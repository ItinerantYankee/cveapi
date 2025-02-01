from rest_framework import serializers
from .models import Cve

class CveSerializer(serializers.ModelSerializer):
    # Converts Django models into serialized data such as JSON and back
    class Meta:
        # Provides metadata about parent class
        # Configures model behavior, set-model wide options, define metadata about class, specify how class should be handled
        model = Cve
        fields = '__all__'