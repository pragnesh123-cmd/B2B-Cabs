from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from apps.booking.models import ConfirmBooking, PostBooking
from apps.accounts.models import User
from apps.accounts.api_v1.serializers import UserReadSerializer,UserCreateSerializer
import requests
import json
import razorpay

client = razorpay.Client(auth=("rzp_test_XKDxN06zGKh0EY", "6ssNF37cFrPzB1vebbFTHmey"))


class CheckRazorpayAcoountAPIView(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        vendor = User.objects.get(id=user_id)
        data = {}
        if vendor.razorpay_account_id is not None:
            data['valid'] = True
            data['msg'] = 'this vendor Razorpay account already exists'
        else:
            data['valid'] = False   
            data['msg'] = 'this vendor Razorpay account does not exists, please create first razorpay account then you access to this permissions' 
        return Response(data)

class CreateRazorpayAcoountAPIView(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # vendor_id = self.request.data.get("vendor_id")
        vendor = User.objects.get(id=request.user.id)

        business_name = self.request.data.get("business_name")
        business_type = self.request.data.get("business_type")
        ifsc_code = self.request.data.get("ifsc_code")
        beneficiary_name = self.request.data.get("beneficiary_name")
        account_type = self.request.data.get("account_type")
        account_number = self.request.data.get("account_number")

        url = "https://api.razorpay.com/v1/beta/accounts/"
        data = {
           "name":f"{vendor.get_full_name()}",
           "email":f"{vendor.email}",
           "tnc_accepted":True,
           "account_details":{
              "business_name":business_name,  #"Acme Corporation"
              "business_type":business_type,  #"individual"
           },
           "bank_account":{
              "ifsc_code":ifsc_code,
              "beneficiary_name":beneficiary_name,
              "account_type":account_type,  #"current"
              "account_number":int(account_number)
           }
        }
        headers = {"Content-type": "application/json"}
        r = requests.request("POST",url, data=json.dumps(data), headers=headers,auth=("rzp_test_XKDxN06zGKh0EY","6ssNF37cFrPzB1vebbFTHmey"))
        vendor.razorpay_account_id=r.json().get("id")
        vendor.save()
        return Response()


class PaymentLinkCreateAPIView(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        vendor = User.objects.get(id=request.user.id)
        postbooking_id = self.request.data.get("postbooking_id")
        confirm_booking = ConfirmBooking.objects.create(vendor_id=request.user.id,postbooking_id=postbooking_id)
        r = client.payment_link.create({
            "upi_link": False,
            "amount": 500,
            "currency": "INR",
            "accept_partial": True,
            "first_min_partial_amount": 100,
            "description": "For XYZ purpose",
            "customer": {
                "name": f"{vendor.get_full_name()}",
                "email": f"{vendor.email}",
                "contact":f"{vendor.phone_number}"
            },
            "notify": {
                "sms": True,
                "email": True
            },
            "reminder_enable": True,
            "notes": {
                "policy_name": "Jeevan Bima"
            },
            "callback_url":"https://www.test.com/?confirm_booking_id=f'{confirm_booking.id}'",
            "callback_method":"get",
        })
        print(r)
        return Response()


# client.utility.verify_payment_link_signature({
#    'payment_link_id': payment_link_id,
#    'payment_link_reference_id': payment_link_reference_id,
#    'payment_link_status':payment_link_status,
#    'razorpay_payment_id': razorpay_payment_id,
#    'razorpay_signature': razorpay_signature
#    })

class PaymentConfirmAPIView(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        vendor = User.objects.get(id=request.user.id)
        confirm_booking_id = self.request.data.get("confirm_booking_id")
        postbooking = ConfirmBooking.objects.get(id=confirm_booking_id)

        # confirm_booking = ConfirmBooking.objects.get(vendor_id=request.user.id,postbooking_id=postbooking_id)
        url = 'https://api.razorpay.com/v1/payments/pay_JEUqs0NU10q3dJ/transfers/'
        data = {
            "transfers": [
                {
                    "account": f"{postbooking.razorpay_account_id}",
                    "amount": 100,
                    "currency": "INR",
                    "notes": {
                        "name": "Gaurav Kumar",
                        "roll_no": "IEC2011025"
                    },
                    "linked_account_notes": [
                        "roll_no"
                    ],
                    "on_hold": True,
                    "on_hold_until": 1671222870
                }
            ]
        }
        headers = {"Content-type": "application/json"}
        r = requests.request("POST",url, data=json.dumps(data), headers=headers,auth=("rzp_test_XKDxN06zGKh0EY","6ssNF37cFrPzB1vebbFTHmey"))
        
        return Response()

