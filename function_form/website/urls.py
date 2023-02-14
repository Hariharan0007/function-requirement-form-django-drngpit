from django.urls import path

from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('a/',views.add_new,name='add_new_staff'),
    path('u/',views.admin,name='admin'),
    path('h/',views.function_home,name='function_home'),
    path('ap/',views.function_admin,name='function_admin'),
    path('p/',views.change_password,name='change_password'),
    path('e/',views.edit_function,name='edit_function'),
    path('check_availability/',views.check_availability,name='check_availability'),
    path('download',views.download,name='download'),
    path('d/',views.delete,name= 'delete'),
    path('submit/',views.submit,name='submit'),
    path('edit/',views.edit_form_test,name='edit_form_test'),
]