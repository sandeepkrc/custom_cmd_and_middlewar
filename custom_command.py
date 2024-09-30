#  in app directory create a file with name of command name and write the below code
#


from django.core.management.base import BaseCommand,CommandError
import os

dirs = [
    "media/",
    "archive",
    "media/csvfiles",
    "media/pdfs",
    "media/compare",
    "media/swaggerfiles",
    "media/wsdlinputfiles",
    "media/mitm_csvfiles"
    ]

def general_directory(list_of_directory):

    for dir in list_of_directory:
        try:
            os.makedirs(dir,exist_ok=True)    
        except Exception as e:
            pass

class Command(BaseCommand):

    """Command for creating a new directory
     for logs."""
    
    help = "Create directory for logs "
    def handle(self, *args, **kwargs):
        try:
            general_directory(dirs)
        except Exception as e:
            raise CommandError("Failed to create directory",e)
        self.stdout.write("Creating media directory >>> >>>")




##############################################  custom middleware   #########################################


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'fuzzer.components.authtoken.TokenBlacklistMiddleware',
]





from django.contrib.auth.middleware import MiddlewareMixin
from django.http import HttpResponseForbidden

from rest_framework_simplejwt.tokens import UntypedToken


class TokenBlacklistMiddleware(MiddlewareMixin):
    """ Middleware for handling token blacklist
        return None if token is valid and
        returns Token is blacklisted
    """

    def process_request(self, request):
        
        header = request.META.get('HTTP_AUTHORIZATION')
        if header:
            try:
                token= get_token(header)
                UntypedToken(token)  # Decode the token without verifying signature
                if BlacklistedToken.objects.filter(token=token).exists():
                    return HttpResponseForbidden('Token is blacklisted')
            except:
                pass
        return None
############################################################################ 
# or
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('CustomMiddleware: Before the request is processed')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print('CustomMiddleware: After the request is processed')

        return response
