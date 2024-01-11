from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken


class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        authentication = JWTAuthentication()
        try:
            authentication_data = authentication.authenticate(request)
            if authentication_data:
                user, _ = authentication_data
                request.user = user
        except InvalidToken as e:
            return JsonResponse(data=e.detail, status=e.status_code)

        return self.get_response(request)