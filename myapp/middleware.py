import datetime
from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin


class TimeOutMiddleware(MiddlewareMixin):

    def process_request(self, request):
        to_logout = False
        if not request.user.is_superuser and request.user.is_authenticated:
            if 'beginSession' in request.session:
                time_has_passed = datetime.datetime.now().timestamp() - request.session['beginSession']
                if time_has_passed > 60 * 5:
                    del request.session['beginSession']
                    to_logout = True
            else:
                request.session['beginSession'] = datetime.datetime.now().timestamp()
            if to_logout:
                logout(request)
        return self.get_response(request)
