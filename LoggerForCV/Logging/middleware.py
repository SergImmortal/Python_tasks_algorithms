from django.utils.deprecation import MiddlewareMixin
import datetime
from .models import Logging

class TrackUsersMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        referrer = str(request.META.get('HTTP_REFERER'))
        time = datetime.datetime.now()
        L = Logging(ip=ip, referrer=referrer)
        L.save()


