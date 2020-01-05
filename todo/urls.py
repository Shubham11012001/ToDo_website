from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name="index"),
    path('complete/<todo_id>', views.MarkCompleteTodo, name="complete"),
    path('add', views.AddNewTodo, name='add'),
    path('incomplete/<todo_id>', views.MarkIncompleteTodo, name='incomplete'),
    path('delete', views.DeleteTodo, name='delete'),
]
