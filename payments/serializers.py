from rest_framework import serializers

from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    PERIOD_FORMAT = '%m/%Y'
    
    period = serializers.DateTimeField(input_formats=[PERIOD_FORMAT, ], required=False)

    class Meta:
        model = Payment
        fields = ['user', 'period', 'status', 'msg']

    def validate(self, attrs):
        if attrs['status'] == Payment.STATUS_OK  and attrs.get('period', None) is None:
            raise serializers.ValidationError(
                {'period': 'Если платеж имеет статус ok, тогда должен быть указан период'})
        if attrs['status'] == Payment.STATUS_ERROR and attrs.get('msg', None) is None:
            raise serializers.ValidationError(
                {'msg': 'Если платеж имеет статус error, тогда должено быть указано сообщение'})
        return attrs
