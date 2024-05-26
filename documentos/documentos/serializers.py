from rest_framework import serializers
from . import models


class documentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'file','uploaded_at',)
        model = models.document