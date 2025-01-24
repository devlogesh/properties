from functools import wraps
from django.http import JsonResponse
from django.conf import settings
from propertiesapp.models import AccessToken

# Add your secret key to Django settings
SECRET_KEY_OVERRIDE = "enga_area_ulla_varadha"

def bearer_token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check for the secret key in the request headers
        secret_key = request.headers.get("X-Secret-Key")
        if secret_key == SECRET_KEY_OVERRIDE:
            # Bypass authentication if secret key is valid
            return view_func(request, *args, **kwargs)
        
        # Check for Bearer token in the Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Authentication credentials were not provided."}, status=401)
        
        # Extract the token
        token = auth_header.split(" ")[1]
        
        # Validate the token (custom logic here, e.g., database lookup)
            
        
        token = AccessToken.objects.filter(key=token)
        print(token,'po')
        if len(token) > 0:
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({"error": "Invalid or expired token."}, status=403)
        
    
    return _wrapped_view
