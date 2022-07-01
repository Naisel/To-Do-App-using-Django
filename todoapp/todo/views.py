

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect 
from django.urls import reverse_lazy

from .models import Task

# Create your views here.
def home(request):
    return render(request, 'home.html')

class TaskList(ListView):
	model = Task
	template_name = 'user.html'
	context_object_name = 'tasks'
	paginate_by = 10
	ordering = ['-create_date']

class TaskDetail(DetailView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task'
    pk_url_kwarg = 'pk'


class TaskCreate(CreateView):
	model =  Task
	template_name = 'task.html'
	context_object_name = 'task-create'
	fields = '__all__'
	success_url = reverse_lazy('tasks') 
	
