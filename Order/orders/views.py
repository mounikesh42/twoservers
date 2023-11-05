import requests
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
JWT_authenticator = JWTAuthentication()
from .models import Order
from rest_framework.response import Response




class CreateObjectWithToken(APIView):
    def post(self, request):
        print("cant access this view")
        token = request.data.get('token', '')
        order_value = request.data.get('order_value', '')
        order_shipped = request.data.get('order_shipped', '')
        order_quantity  = request.data.get('order_quantity', '')
        if not token:
            return Response({'detail': 'Token not provided'})


        print(token)
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('http://localhost:8000/api/auth/user/details/', headers=headers)
        print(response)

        user_id = response.json().get('userid')  
        new_object = Order(
            user=user_id,
            order_value=order_value,
            order_shipped=order_shipped,
            order_quantity=order_quantity
        )
        new_object.save()  

        new_object.slug = str(new_object.id)
        new_object.save()  

        return HttpResponse(new_object)




class GetOrdersByUser(APIView):
    def get(self, request):
        token = request.data.get('token', '')

        if not token:
            return Response({'detail': 'Token not provided'}, status=status.HTTP_BAD_REQUEST)

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('http://localhost:8000/api/auth/user/details/', headers=headers)

        if response.status_code == 200:
            user_id = response.json().get('userid')  

            orders = Order.objects.filter(user=user_id)
            order_data = [
                {
                    "order_value": order.order_value,
                    "order_shipped": order.order_shipped,
                    "order_quantity": order.order_quantity,
                    "slug":order.slug
                }
                for order in orders
            ]

            return Response(order_data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Failed to retrieve orders'}, status=response.status_code)