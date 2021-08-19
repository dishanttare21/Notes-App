from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notedetails/<int:noteid>/',views.note_details,name='notedetails'),
    path('delete/<int:noteid>/',views.delete,name='delete'),
    path('update/<int:noteid>/',views.update,name='update'),
]
