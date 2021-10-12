from django.http import HttpResponse

def howru(request):
    print (dir(request))
    return HttpResponse("<h1>Ho ho ho!</h1>")
