from django.shortcuts import render

def posts_list(request):
    n = ['masha','olya','elena']
    return render(request,'feed/index.html', context = {'names' : n })
# Create your views here.
