from django.shortcuts import render
from random import randint, choice
from string import digits, ascii_letters

# Create your views here.

def index(request):
    int_page = randint(100, 10000)
    str_page = ''.join(choice(digits+ascii_letters) for i in range(randint(5, 12)))
    return render(request, 'index.html', {
        'int_page': int_page,
        'str_page': str_page,
    })


def int_url(request, page):
    print(page)
    return render(request, 'int_url.html', {
        'page': page
    })


def str_url(request, page):
    print(page)
    return render(request, 'str_url.html', {
        'page': page
    })
