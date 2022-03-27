from rest_framework import serializers

from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=256)
    person = serializers.CharField(max_length=256)
    file_size = serializers.IntegerField()

    class Meta:
        model = Document
        fields = '__all__'
