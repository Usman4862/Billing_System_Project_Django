from django.urls import path
from . import views

app_name = 'bill'

urlpatterns = [
    path('',views.index,name='index'),
    path('bill/',views.cal_amount,name='cal_amount'),
    path('test/',views.test_iterations,name='test_iterations'),
]
