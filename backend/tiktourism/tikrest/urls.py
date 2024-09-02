from django.urls import path, register_converter

from . import views, converts

register_converter(converts.FloatUrlParameterConverter, 'float')

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('restaurantUpdate/<str:name>&<float:rating>&<float:prox>', views.restaurantUpdate, name='restaurantUpdate'),
    path('updaterecord/<str:name>&<float:rating>&<float:prox>', views.updaterecord, name='updaterecord'),
    path('updatelike/<str:name>&<float:rating>&<float:prox>', views.updatelike, name='updatelike'),
]