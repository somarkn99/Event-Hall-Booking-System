import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response = {
            'success': False,
            'message': '',
            'errors': response.data
        }

        if isinstance(response.data, dict):
            if 'detail' in response.data:
                custom_response['message'] = response.data['detail']
                custom_response['errors'] = None
            else:
                custom_response['message'] = "Validation Error"

        response.data = custom_response
    else:
        logger.exception('Unhandled exception occurred', exc_info=exc)

        response = Response({
            'success': False,
            'message': 'Internal server error',
            'errors': None
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
