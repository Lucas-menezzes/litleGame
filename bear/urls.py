from django.contrib import admin
from django.urls import path
from .views.create_player import create_player, get_player
from .views.mk_deposit import mk_deposit


urlpatterns = [
    path("admin/", admin.site.urls),
    path("create_player", create_player, name='create_player'),
    path("get_player", get_player, name='get_player'),
    path("mk_deposit", mk_deposit, name='mk_deposit')

]
