import json
from datetime import datetime
from rest_framework import viewsets, serializers
from webapp.models import GithubEvent


class GithubEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GithubEvent

    def to_internal_value(self, data):
        return {
            'created_on': datetime.now(),
            'payload': json.dumps(data)
        }

    def create(self, validated_data):
        return GithubEvent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.payload = validated_data
        return instance

    def to_representation(self, instance):
        if not instance:
            return None
        instance.payload = json.loads(instance.payload)
        return super(GithubEventSerializer, self).to_representation(instance)


class GithubEventViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Github events.
    """
    queryset = GithubEvent.objects.all()
    serializer_class = GithubEventSerializer
