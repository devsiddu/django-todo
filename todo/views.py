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