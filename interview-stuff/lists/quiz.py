print([x for x in range(1,6) if x&1])
print(1&1)


# myapp/middleware.py
class MyCustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed before the view is called
        # For example, you can perform authentication checks here

        response = self.get_response(request)

        # Code to be executed after the view is called
        # For example, you can modify the response or perform additional tasks

        return response
    
# settings.py
MIDDLEWARE = [
    # Other middleware classes...
    'myapp.middleware.MyCustomMiddleware',
]