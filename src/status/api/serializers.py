from rest_framework import serializers

from accounts.api.serializers import UserPublicSerializer
from status.models import Status


class StatusInlineUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'content',
            'image'
        ]
        
        
class StatusSerializer(serializers.ModelSerializer):
    user    = UserPublicSerializer(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
        
        read_only_fields = ['user']