class CustomMIMEMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.endswith(".js"):
            response["Content-Type"] = "application/javascript"
        return response
