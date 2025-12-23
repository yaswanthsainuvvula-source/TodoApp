from django.shortcuts import render,get_object_or_404,redirect
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def todo_page(request, task_id=None):
    edit_task = None

    if task_id:
        edit_task = get_object_or_404(Todo, id=task_id, user=request.user)

    if request.method == 'POST':
        task_text = request.POST.get('task')

        if edit_task:
            edit_task.task = task_text
            edit_task.save()
        else:
            if task_text:
                Todo.objects.create(user=request.user, task=task_text)

        return redirect('todo_page') 
    tasks = Todo.objects.filter(user=request.user)
    return render(request, 'app2/todopage.html', {'tasks': tasks, 'edit_task': edit_task})



def delete_task(request,task_id):
    task= get_object_or_404(Todo,id=task_id,user=request.user)
    task.delete()
    return redirect('todo_page')