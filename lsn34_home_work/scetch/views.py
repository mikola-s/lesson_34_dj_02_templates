from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def int_url(request, page):  # , *args, **kwargs):  # , int_url_val=100):
    print(page)
    return render(request, 'int_url.html', {
        'page': page
    })


def str_url(request, page):  # , str_url_val='qwerty'):
    print(page)
    return render(request, 'str_url.html', {
        'page': page
    })
