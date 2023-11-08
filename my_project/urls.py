"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from ma_app.views import home,profile
from shop.views import shop_home
from game.views import game_home
from grocery_app.views import grocery_shop
from phone_app.views import apple_phone
from sport.views import play,quit
from tennis.views import tennis_shop
from dating_app.views import dating_shop
from storefront.views import say_hello, say_item, say_search, say_test
from pages.views import hello_book, shop_item, shop_search, shop_test 


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home),
    path('profile/', profile),
    path('shop/', shop_home),
    path('game/', game_home),
    path('grocery_app/', grocery_shop),
    path('phone_app/', apple_phone),
    path('play/', play),
    path('quit/', quit),
    path('tennis/', tennis_shop),
    path('dating_app/', dating_shop),
    path('storefront/', say_hello),
    path('storefront/<int:item_id>/', say_item),
    path('storefront/<str:term>/', say_search),
    re_path('teststorefront/(.*)/', say_test),
    path('pages/', hello_book),
    path('pages/<int:item_id>/', shop_item),
    path('pages/<str:term>/',shop_search),
    re_path('testpages/(.*)/', shop_test)

]


