

# from multiprocessing import context
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.http import HttpResponseRedirect 
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from psutil import users


from .models import Task






# Create your views here.


class RegisterPage(FormView):
	template_name = 'register.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True
	success_url = reverse_lazy('tasks') 

	def form_valid(self, form):
		users = form.save()
		if users is not None:
			login(self.request, users)
		return super(RegisterPage, self).form_valid(form)

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('tasks')

		return super(RegisterPage, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
	template_name = 'login.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('tasks')



def home(request):
    return render(request, 'home.html')

class TaskList(LoginRequiredMixin, ListView):
	model = Task
	template_name = 'user.html'
	context_object_name = 'tasks'
	# paginate_by = 10
	ordering = ['-create_date']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tasks'] = context['tasks'].filter(users=self.request.user)
		return context

# class TaskDetail(DetailView):
#     model = Task
#     template_name = 'task.html'
#     context_object_name = 'task'
#     pk_url_kwarg = 'pk'


class TaskCreate(LoginRequiredMixin, CreateView):
	model =  Task
	template_name = 'task.html'
	context_object_name = 'task-create'
	fields = ['title', 'description', 'is_completed', 'create_date']
	success_url = reverse_lazy('tasks') 

	def form_valid(self, form):
		form.instance.users = self.request.user
		return super(TaskCreate, self).form_valid(form)
	
class TaskUpdate(LoginRequiredMixin, UpdateView):
	model = Task
	context_object_name = 'update'
	template_name = 'task.html'
	fields = '__all__'
	success_url = reverse_lazy('tasks') 

class TaskDelete(LoginRequiredMixin, DeleteView):
	model = Task
	context_object_name = 'task'
	success_url = reverse_lazy('tasks')
	template_name = 'task.html'






