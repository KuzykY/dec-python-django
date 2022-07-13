from rest_framework.response import Response
from rest_framework.views import exception_handler

from core.enums.error_enum import ErrorEnum


def custom_error_handler(exp: Exception, content: dict) -> Response:
    handlers = {
        'JwtException':_jwt_validate_error
    }
    response = exception_handler(exp, content)
    exp_class = exp.__class__.__name__

    if exp_class in handlers:
        function = handlers[exp_class]
        return function(exp, content)

    return response


def _jwt_validate_error(exp: Exception, content: dict) -> Response:
    return Response(ErrorEnum.JWT.msg, ErrorEnum.JWT.code)
