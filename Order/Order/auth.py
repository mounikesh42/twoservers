# import jwt
# from django.contrib.auth import get_user_model
# from django.conf import settings

# User = get_user_model()

# class JWTAuthentication:
#     def authenticate(self, request):
#         auth_header = request.META.get('HTTP_AUTHORIZATION')
#         if not auth_header:
#             return None

#         try:
#             _, token = auth_header.split()
#             payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#             user_id = payload.get('user_id')
#             user = User.objects.get(pk=user_id)
#             return (user, None)
#         except jwt.ExpiredSignatureError:
#             return None
#         except jwt.DecodeError:
#             return None
#         except User.DoesNotExist:
#             return None
