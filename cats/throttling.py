import datetime

from rest_framework import throttling


class WorkingHoursRateThrottle(throttling.BaseThrottle):

    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        if now >= 18 and now < 19:
            return False
        return True