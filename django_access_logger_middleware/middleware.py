import json
from django.core.files.base import File
from django.contrib.auth.models import AnonymousUser
from django_access_logger_middleware.models import AccessLogs
from django.contrib.auth import get_user_model


class AccessLogsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)

        file_params = None
        if request.FILES:
            file_params = ', '.join(['({})'.format(file_path) for file_path in request.FILES])

        view_name = ''
        try:
            view_name = request.resolver_match.func.__name__
        except:
            pass
        data = ''
        try:
            data = repr(response.data)
        except:
            pass
        UserModel = get_user_model()
        r = AccessLogs.objects.create(
            url_path=request.path,
            view_name=view_name,
            method=request.method,
            host_ip=request.META.get('REMOTE_ADDR'),
            http_x_forwarded_for=request.META.get('HTTP_X_FORWARDED_FOR'),
            query_params=repr([(item, value if not isinstance(value, File) else value.name) for item, value in request.GET.items()]),
            form_data=repr([(item, value if not isinstance(value, File) else value.name) for item, value in request.POST.items()]),
            file_params=file_params,
            accessed_by=request.user if type(request.user)==UserModel else None,
            reponse = data,
            response_status_code = response.status_code
        )
        
        return response
