from dj_rest_auth.views import django_logout

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def logout_view(request):
    if request.method == "POST":
        django_logout(request)
        return redirect("/")
    return redirect("/")
