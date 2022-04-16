from django.shortcuts import redirect


# Middleware for Author Model.
def authmiddleware(get_response):
    def middleware(request):
        #print(request.session.get('customer'))
        return_url = request.META['PATH_INFO']
        #print(request.META['PATH_INFO'])
        if not request.session.get('auth_id'):
            return redirect(f'/login?return_url={return_url}')
        response = get_response(request)
        return response

    return middleware
