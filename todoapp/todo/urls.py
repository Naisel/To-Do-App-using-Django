from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home.html', views.home),
    path('user/', views.TaskList.as_view(), name='tasks'),
    # path('user/task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('user/task/<int:pk>/', views.TaskDelete.as_view(), name='task'),
    path('user/create-task/', views.TaskCreate.as_view(), name='task-create'),
    path('user/update-task/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),

]
