from django.http import JsonResponse
import jwt
from functools import wraps
from setup.settings import JWT_SECRET

def jwt_auth_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        token = request.headers.get('Authorization', None)
        if not token:
            return JsonResponse({'error': 'Token faltando'}, status=401)

        try:
            token = str(token).replace('Bearer ', '')
            payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            request.jwt_payload = payload

        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token expirou'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': f'Token Invalido'}, status=401)

        return view_func(request, *args, **kwargs)
    return wrapped_view
