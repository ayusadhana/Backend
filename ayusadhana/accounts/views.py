# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CustomUser
from .utils import generate_otp, otp_sender


@api_view(['POST'])
def user_registration(request):
    try:
        # Step 1: Get first name and phone number
        first_name = request.data.get('first_name')
        phone_number = request.data.get('phone_number')
        if not first_name or not phone_number:
            return Response({"error": "First name and phone number are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Step 2: Check if phone number already exists
        if CustomUser.objects.filter(phone_number=phone_number).first():
            return Response({"error": "Phone number already registered. Please log in instead."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Step 3: Generate OTP and send
        otp, timestamp = generate_otp()
        otp_sender(phone_number, otp)
        print(otp)

        # Step 4: Register user
        user = CustomUser.objects.create(first_name=first_name, phone_number=phone_number, otp=otp)
        print(user)
        user.save()
        return Response({"message": "OTP sent successfully"}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def verify_otp(request):
    phone_number = request.data.get('phone_number')
    otp = request.data.get('otp')

    try:
        user_details = CustomUser.objects.get(phone_number=phone_number)
        if user_details.otp != otp:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        # Mark the OTP as verified or perform any additional actions here
        return Response({'message': 'OTP verified successfully'}, status=status.HTTP_)

    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
