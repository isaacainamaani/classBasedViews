from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy
from . models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'taskForm.html'

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'taskForm.html'