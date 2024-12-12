from django.urls import path
from . import views

urlpatterns = [
    path('todo_list/', views.todo_list_view, name='todoList'),
    path('todo_list/<int:id>/', views.todo_detail_view, name='todo_detail'),
    path('todo_list/<int:id>/update/', views.update_todo_view, name='update_todo'),
     path('todo_list/<int:id>/delete/', views.delete_todo_view, name='delete_todo'),
    path('create_todo/', views.create_todo_view, name='createTodo'),
]