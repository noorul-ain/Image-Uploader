from django.urls import path 
from . import views 

urlpatterns = [
    path('hm/', views.home, name='home'),
    # path('st/', views.student_data, name='student_data')
]