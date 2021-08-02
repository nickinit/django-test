from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world!')

def bot_input(request):
    return HttpResponse('Hi!')