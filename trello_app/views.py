from django.shortcuts import render, redirect
from trello_app.models import Tasks, TaskList
from .forms import TaskListForm, TaskForm

# Create your views here.
def index(request):
    tasks = Tasks.objects.all()
    task_lists = TaskList.objects.all()
    return render(request, 'trello_app/index.html', {"tasks": tasks, "task_lists": task_lists})

def add_task_list(request):
    if request.method == "POST":
        name = request.POST['name']
        created_at = request.POST['created_at']
        task_list = TaskList(name=name, created_at=created_at)
        task_list.save()
        return redirect('/dashboard')
    return render(request, 'trello_app/add_task_list.html')


def add_task_list_2(request):
    if request.method == "POST":
        form = TaskListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    else:
        form = TaskListForm()

    return render(request, 'trello_app/add_task_list_2.html', {'form':form} )
    
def add_task(request):
    if request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    else:
        form = TaskForm()
    return render(request, 'trello_app/add_task.html', {'form':form} )


    