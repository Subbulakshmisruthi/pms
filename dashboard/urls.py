from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('/',views.dashboard,name="dashboard"),
    path('/projects',views.projects,name="projects"),
    path('/tasks',views.tasks,name="tasks"),
    path('/analytics',views.analytics,name="analytics"),
    path('/settings',views.settings,name="settings"),
    path('/addproject',views.addProject,name="addProject"),
    path('/addtask',views.addTask,name="addTask"),
    path('/editproject/<str:pk>/',views.editProject,name="editProject"),
    path('/deleteproject/<str:pk>/',views.deleteproject,name="deleteproject"),
    path('/edittask/<str:pk>/',views.editTask,name="editTask"),
    path('/deletetask/<str:pk>/',views.deletetask,name="deletetask"),
]