# Create your views here.
from django.http import HttpResponse

def dashboard(request):
    dashboard = ""
    return HttpResponse(dashboard)

