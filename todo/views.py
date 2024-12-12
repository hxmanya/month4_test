from django.shortcuts import render, redirect, get_object_or_404
from todo.models import TodoModel
from todo.forms import TodoForm


#create todo
def create_todo_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todoList')

    else:
        form = TodoForm()
    return render(request, template_name='todo/create_todo.html', context={'form': form})



#read todo
def todo_list_view(request):
    if request.method == 'GET':
        todo_list = TodoModel.objects.all().order_by('-id')
        context = {
            'todo_list': todo_list
        }
        return render(request, template_name='todo/todo_list.html', context=context)

#read detail todo
def todo_detail_view(request, id):
    if request.method == 'GET':
        todo_id = get_object_or_404(TodoModel, id=id)
        context = {'todo_id': todo_id}
        return render(
            request, 
            template_name='todo/todo_detail.html',
            context=context          
                      )

#update todo
def update_todo_view(request, id):
    todo_id = get_object_or_404(TodoModel, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo_id)
        if form.is_valid():
            form.save()
            return redirect('todoList')
    else:
        form = TodoForm(instance=todo_id)
    return render(request, 
                  template_name='todo/todo_update.html',
                  context={
                      "todo_id": todo_id,
                      "form": form
                  }
                  )
#delete todo
def delete_todo_view(request, id):
    todo_id = get_object_or_404(TodoModel, id=id)
    todo_id.delete()
    return redirect('todoList')