
from django.contrib import admin
from django.urls import path
from my_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-two/<int:num1>/<int:num2>/', addition_view ,name='add') ,
    path('area-of-circle/<int:radius>/', area_of_circle ,name='area') ,
    path('area_of_rectangle/int:l>/<int:b>/', area_of_rectangle, name='area_of_rectangle') ,
    path('area_of_triangle/int:base>/<int:height>/', area_of_triangle, name='area_of_triangle') ,
    path('area_of_square/int:side>/', area_of_square, name='area_of_square') ,
    path('multiply/<int:num1>/<int:num2>/', multiplication_view ,name='multiply') ,
    path('divide/<int:num1>/<int:num2>/', division_view ,name='divide') ,
    path('subtract/<int:num1>/<int:num2>/', subtraction_view ,name='subtract') ,
    path('area_of_cube/int:side>/', area_of_cube, name='area_of_cube') ,
    path('prime-check/<int:num>/', prime_check_view, name='prime_check') ,

 
]
