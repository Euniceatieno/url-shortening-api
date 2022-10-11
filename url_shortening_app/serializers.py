from rest_framework import serializers

from .models import OriginalUrl


class OriginalUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginalUrl
        fields = ("original_url_id", "original_url", "date_created")
