from django.shortcuts import render


# Create your views here.

def index(request):
    int_page = 100
    str_page = 'qwerty'
    return render(request, 'index.html', {
        'int_page': int_page,
        'str_page': str_page,
    })


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
