import django_filters
from rest_framework.viewsets import ModelViewSet

from study.seriallizers.payments import PaymentsBaseSerializer, Payments


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsBaseSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('type', 'payment_type')
