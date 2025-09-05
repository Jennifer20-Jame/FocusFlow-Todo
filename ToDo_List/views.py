from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from .forms import TaskForm
from .models import Task


@login_required
def home(request):
    user_tasks = Task.objects.filter(user=request.user)
    total_tasks = user_tasks.count()
    completed_tasks = user_tasks.filter(status="completed").count()
    pending_tasks = user_tasks.filter(status="pending").count()

    context = {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
    }

    return render(request, template_name='ToDo_List/home.html', context=context)

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, template_name='ToDo_List/task_list.html', context=context)

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status:
            task.status = new_status
            task.save()
            return redirect('view-task', pk=task.id)
    context =  {
        'task': task,
        'status_choices': Task._meta.get_field('status').choices 
    }
    return render(request, template_name='ToDo_List/task_detail.html', context=context)

@login_required
def task_done(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == 'POST':
        task.done = not task.done  
        if task.done:
            task.status= 'completed'
        else:
            task.status='pending'
        task.save()
        return redirect('task-list')


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
        context = {'form': form}
        return render(request, template_name='ToDO_List/add_task.html', context=context)

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
            form = TaskForm(instance=task)
            context = {'form': form}
            return render(request, template_name='ToDO_List/edit_task.html', context=context)

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    else:
        context = {'task': task}
        
        return render(request, template_name='ToDO_List/delete_task.html', context=context)
        
