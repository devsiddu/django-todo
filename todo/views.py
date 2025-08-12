from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Task
# Create your views here.

def add_task(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def update_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.is_completed = True
    task.save()
    return redirect('home')

def unmark_task(request,id):
    task = get_object_or_404(Task, pk=id)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request,id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        updated_task = request.POST['task']
        task.task = updated_task
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task
        }
    return render(request, 'edit_task.html', context)

def delete_task(request, id):
    task =  get_object_or_404(Task,pk=id)
    task.delete()
    return redirect('home')