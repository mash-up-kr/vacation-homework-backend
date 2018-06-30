from rest_framework import serializers
from . import models


class questionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = (
            'message',
        )
