from rest_framework import serializers

from .models import Document

class DocumentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    operator_id = serializers.IntegerField()

    def ceate(self, validated_data):
        return Document.objects.create(**validatet_data)
