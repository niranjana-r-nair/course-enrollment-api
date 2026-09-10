from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from enrollment.models import Enrollment
from enrollment.serializers import EnrollmentSerializer
from enrollment.permissions import IsStudent
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status



import razorpay

class EnrollmentViewSet(viewsets.ModelViewSet):

    queryset=Enrollment.objects.all()
    serializer_class=EnrollmentSerializer
    permission_classes=[IsStudent]

    def perform_create(self,serializer):
        course=serializer.validated_data['course']
        amount=course.fee
        enrollment=serializer.save(student=self.request.user,amount=amount)
        client=razorpay.Client(auth=('rzp_test_TZ7X8lFGtbnbC3','t70KTAiASGYyYQ0AYHtbjiGa'))
        print(client)
        response_payment=client.order.create(dict(amount=amount*100,currency="INR"))
        print(response_payment)

        enrollment.order_id=response_payment['id']
        enrollment.save()
        return enrollment

class Verifypayment(APIView):
    permission_classes=[IsStudent]

    def post(self,request):
        booking_id = request.data['booking_id']
        payment_id=request.data['razorpay_payment_id']
        order_id=request.data['razorpay_order_id']
        signature=request.data['razorpay_signature']
        enrollment=Enrollment.objects.get(order_id=order_id,student=request.user)

        #payment verification
        try:
            client=razorpay.Client(auth=('rzp_test_TZ7X8lFGtbnbC3', 'rzp_test_TZ7X8lFGtbnbC3'))

            client.utility.verify_payment_signature({"razorpay_order_id": order_id,
                "razorpay_payment_id":payment_id,
                "razorpay_signature":signature})

            enrollment.status="completed"
            enrollment.save()
            enrollment.course.available_seats=(enrollment.course.available_seats - 1)
            enrollment.course.save()

            return Response({"msg":"payment successfully completed"},status=status.HTTP_200_OK)
        except:
            return Response(
                {"msg":"payment verification failed"},status=status.HTTP_400_BAD_REQUEST)