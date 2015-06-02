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
            'payload': json.dumps(data, indent=4)
        }

    def create(self, validated_data):
        return GithubEvent.objects.create(**validated_data)


class GithubEventViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Github events.
    """
    queryset = GithubEvent.objects.all()
    serializer_class = GithubEventSerializer
