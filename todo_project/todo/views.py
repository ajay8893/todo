from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import todo
from .forms import Todoform

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'todo/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def task_list(request):
    tasks = todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = Todoform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = Todoform()
    return render(request, 'todo/task_form.html', {'form': form})


@login_required
def task_update(request, task_id):
    task = get_object_or_404(todo, id=task_id, user=request.user)
    if request.method == 'POST':
        form = Todoform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = Todoform(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})


@login_required
def task_delete(request, task_id):
    task = get_object_or_404(todo, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_delete.html', {'task': task})


@login_required
def task_complete(request, task_id):
    task = get_object_or_404(todo, id=task_id, user=request.user)
    task.complete = not task.complete
    task.save()
    return redirect('task_list')
