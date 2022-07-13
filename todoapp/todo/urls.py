from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'home'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('', views.home, name='home'),
    path('home', views.home),
    path('user/', views.TaskList.as_view(), name='tasks'),
    # path('user/task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('user/task/<int:pk>/', views.TaskDelete.as_view(), name='task'),
    path('user/create-task/', views.TaskCreate.as_view(), name='task-create'),
    path('user/update-task/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
   
]
