from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display/<str:sort_field>/',views.display, name='display'),
    path('search/<str:query_title>/',views.search,name='search')
]