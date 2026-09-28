from datetime import datetime
from time import  perf_counter
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
# class SimpleMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         print("this is process request")
#         print("request path:", request.path)
#         print("request method:", request.method)
#         print("request time:", datetime.now())

#     def process_response(self, request, response):
#         print("this is process response")
#         print("response status code:", response.status_code)
#         print("response time:", datetime.now())
#         return response

# class RequestTimeMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         request.start_time = datetime.now()
#         print(f"Request to {request.path} started at {request.start_time}.")

#     def process_response(self, request, response):
#         if hasattr(request, 'start_time'):
#             end_time = datetime.now()
#             duration = end_time - request.start_time
#             print(f"Request to {request.path} ended at {end_time}")
#             print(f"Request to {request.path} took {duration.total_seconds()} seconds.")
#         return response

# class PerformanceMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         request.start_time = perf_counter()

#     def process_response(self, request, response):
#         if hasattr(request, 'start_time'):
#             end_time = perf_counter()
#             duration = end_time - request.start_time
#             print(f"Request to {request.path} took {duration:.4f} seconds.")
#         return response

# class BlockIPMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         ip_block='127.0.0.2'
#         user_ip=request.META.get('REMOTE_ADDR')
#         if user_ip == ip_block:
#             return HttpResponse("<h1>Your IP address is blocked</h1>")
#         return None

class LongInCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
     if request.path.startswith('/home/'):   
        if not request.user.is_authenticated:
            return HttpResponse("<h1>You must be logged in to access this page.</h1>")
        return None