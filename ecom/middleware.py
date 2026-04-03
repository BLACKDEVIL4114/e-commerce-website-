import binascii
import logging
from django.conf import settings
from django.http import HttpResponseRedirect

logger = logging.getLogger(__name__)

class ClearBadSessionMiddleware:
    """Middleware to catch base64/session decoding errors (e.g. 'Incorrect padding')
    caused by corrupted session cookies. If such an error occurs we remove the
    session cookie and redirect back to the same URL so the request can proceed
    with a clean session."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except (binascii.Error, ValueError) as exc:
            # Only handle decoding/padding related errors
            logger.warning('Clearing corrupted session cookie due to: %s', exc)
            resp = HttpResponseRedirect(request.get_full_path())
            resp.delete_cookie(settings.SESSION_COOKIE_NAME)
            return resp
