from django.http import HttpResponse

def hello(request):
    return HttpResponse ('some text')
