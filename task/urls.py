from django.urls import path
from . import views

urlpatterns = [
   path("", views.home, name="home"),
   path('complete/<int:id>/', views.complete_task, name='complete_task'),
   path('delete/<int:id>/', views.delete_task, name='delete_task'),
   path('undo/<int:id>/', views.undo_task, name='undo_task'),
]
