import logging

from django.http import JsonResponse
from opa_client import OpaClient
from rest_framework import status

from config import settings

from config.messages import OPA_SERVER_ERROR, OPA_ACCESS_ERROR

logger = logging.getLogger('app')


class OpaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.opa_client = OpaClient(host=settings.OPA_HOST, port=settings.OPA_PORT)

    def __call__(self, request):
        data = self.build_opa_data(request)
        try:
            allowed = self.check_opa_permission(data)
        except Exception as e:
            return self.error_response(OPA_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR)

        if not allowed:
            return self.error_response(OPA_ACCESS_ERROR, status.HTTP_403_FORBIDDEN)
        logger.info(f"data --> {data} | result --> {allowed}")
        return self.get_response(request)

    @staticmethod
    def build_opa_data(request):
        return {
            "method": request.method,
            "path": request.path.rstrip("/").strip().split("/")[1:],
            "is_authenticated": request.user.is_authenticated,
            "roles": ['admin'] if request.user.is_superuser else []
        }

    @staticmethod
    def error_response(data, status_code):
        return JsonResponse(data=data, status=status_code)

    def check_opa_permission(self, data):
        response = self.opa_client.check_permission(
            input_data={"input": data},
            policy_name=settings.OPA_POLICY_NAME,
            rule_name=settings.OPA_RULE_NAME,
        )
        return response["result"]
