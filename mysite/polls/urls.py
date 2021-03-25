from django.urls import path
from . import views

urlpatterns = [
    # path() 関数は4つの引数を受け取ります。引数のうち route と view の2つは必須で、kwargs、name の2つは省略可能
    path('', views.index, name='index'),
]