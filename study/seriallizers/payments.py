from rest_framework import serializers

from study.models.payments import Payments


class PaymentsBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = [
            'user',
            'created_at',
            'type',
            'payment_sum',
            'payment_type',
        ]
