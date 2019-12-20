from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    # path("100/", views.int_url, name='int_url'),
    path("<int:page>/", views.int_url, name='int_url'),
    path("<str:page>/", views.str_url, name='str_url'),
    # path("<str:str_url_val>/", views.str_url, name='str_url'),

]
