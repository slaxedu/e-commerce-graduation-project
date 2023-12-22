# middleware.py
from .models import UserAction, Vistor, UserInfo

# class UserInfoMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         self.process_request(request)
#         return response

#     def process_request(self, request):


class UserActionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.process_request(request)
        return response

    def process_request(self, request):
        try:
            user_info=UserInfo.objects.create(
                user = request.user or '',
                cookie = request.COOKIES.get('csrftoken', ''),
                session_id = request.COOKIES.get('sessionid',''),
                os = request.META.get('OS',''),
                name = request.META.get('USERNAME',''),
                computer_name = request.META.get('COMPUTERNAME',''),
                user_agent = request.META.get('HTTP_USER_AGENT', ''),
                ip_address = request.META.get('REMOTE_ADDR', ''),
                referrer = request.META.get('HTTP_REFERER', ''),
            )
            if request.user.is_authenticated:
                action = request.path
                UserAction.objects.create(user=request.user, action=action, user_info=user_info)
            else:
                action =  request.path
                viste = Vistor.objects.create(action=action, user_info=user_info)
        except:    
            if request.user.is_authenticated:
                action = request.path
                UserAction.objects.create(user=request.user, action=action)
            else:
                action =  request.path
                viste = Vistor.objects.create(action=action)
                    
