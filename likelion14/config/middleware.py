import logging

logger = logging.getLogger('django')

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"{request.method} {request.get_full_path()}")

        response = self.get_response(request)

        if response.status_code >= 400:
            logger.warning(f"{request.method} {request.get_full_path()} - {response.status_code}")

        return response
