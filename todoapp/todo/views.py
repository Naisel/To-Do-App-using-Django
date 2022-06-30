
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Task

# Create your views here.
def home(request):
    return render(request, 'home.html')

class TaskList(ListView):
	model = Task
	template_name = 'user.html'
	context_object_name = 'tasks'
	paginate_by = 5
	ordering = ['-create_date']




