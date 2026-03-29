from django.shortcuts import render
from .models import Task
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def home(request):

    if request.method == "POST":

        title = request.POST.get('title')
        if title:
            title = title.title() 
            Task.objects.create(title=title)

    tasks = Task.objects.all()
    return render(request, "home.html", {'tasks' : tasks} )


def complete_task(request,id):
    task = get_object_or_404(Task,id=id)
    task.completed = True
    task.save()
    return redirect('home')

def delete_task(request,id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')

def undo_task(request,id):
    task = get_object_or_404(Task,id=id)
    task.completed = False
    task.save()
    return redirect('home')
