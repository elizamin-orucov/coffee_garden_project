# Capturing the API address of non-logged-in users

def get_ip_address(request):
    forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded_for:
        api = forwarded_for.split(",")[0]
    else:
        api = request.META.get("REMOTE_ADDR")
    return api
