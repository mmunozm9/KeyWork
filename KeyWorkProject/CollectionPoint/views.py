from django.http import HttpResponse

def index(request):
    return HttpResponse("🚀 ¡Bienvenido a KeyWork! La instalación fue exitosa.")
