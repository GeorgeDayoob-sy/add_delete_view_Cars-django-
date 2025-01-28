from django.urls import path , include
from . import views
app_name='pages'

urlpatterns = [
    
    path('',views.list,name="list"),
    path('add/',views.add,name="add"),
    path('delete/',views.delete,name="delete"),
]