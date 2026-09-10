from rest_framework import serializers
from enrollment.models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Enrollment
        fields='__all__'
        read_only_fields=['student','enrollment_date','amount','order_id','status']