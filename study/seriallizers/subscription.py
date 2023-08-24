from rest_framework import serializers

from study.models.subscription import Subscription
from study.validators import validator_scam_url


class SubBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'course', 'is_sub',
        ]