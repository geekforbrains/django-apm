class APMMiddleware:
    def __init_(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # code to execute before view
        print('before request')
        response = self.get_response(request)
        # code to be exucted after the view
        print('after request')
        return response
