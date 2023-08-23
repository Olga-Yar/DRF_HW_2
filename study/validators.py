from rest_framework import serializers


def validator_scam_url(value):
    if 'youtube' not in value.lower():
        raise serializers.ValidationError('Ссылка должна быть только с youtube!')