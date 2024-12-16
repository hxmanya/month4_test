from django.urls import path
from . import views

urlpatterns = [
    path('todo_list/', views.TodoListView.as_view(), name='todoList'),
    path('todo_list/<int:id>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('todo_list/<int:id>/update/', views.UpdateTodoView.as_view(), name='update_todo'),
    path('todo_list/<int:id>/delete/', views.DeleteTodoView.as_view(), name='delete_todo'),
    path('create_todo/', views.CreateTodoView.as_view(), name='createTodo'),
]