from multiprocessing import context
from .forms import CreateProjectForm, CreateTaskForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from home.models import Projects, Tasks
# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    project_obj = Projects.objects.filter(user=request.user)
    count1 = project_obj.count()
    count2 = Tasks.objects.filter(user=request.user).count()
    projects = project_obj.order_by('due')
    context = {'projects_count':count1,'task_count':count2,'projects':projects}
    return render(request,'dashboard\home.html',context)

@login_required(login_url="login")
def projects(request):
    project = Projects.objects.filter(user=request.user)
    context={"projects":project,'page':1}
    return render(request,"dashboard\projects.html",context)

@login_required(login_url="login")
def addProject(request):
    form = CreateProjectForm()
    if request.method == "POST":
        instance_query = request.POST.copy()
        instance_query['user']=request.user
        form = CreateProjectForm(instance_query)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect("projects")
    context = {"form":form,'page':2}
    return render(request,'dashboard\projects.html',context)

@login_required(login_url="login")
def deleteproject(request,pk):
    Projects.objects.get(id=pk).delete()
    return redirect('projects')

@login_required(login_url="login")
def deletetask(request,pk):
    Tasks.objects.get(id=pk).delete()
    return redirect('tasks')

@login_required(login_url="login")
def editProject(request,pk):
    obj = Projects.objects.filter(id=pk).first()
    form = CreateProjectForm(instance = obj)
    if request.method == "POST":
        instance_query = request.POST.copy()
        instance_query['user']=request.user
        form = CreateProjectForm(instance_query,instance = obj)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect("projects")
    context = {"form":form,'page':2}
    return render(request,'dashboard\projects.html',context)

@login_required(login_url="login")
def editTask(request,pk):
    obj = Tasks.objects.filter(id=pk).first()
    form = CreateTaskForm(instance = obj)
    if request.method == "POST":
        instance_query = request.POST.copy()
        instance_query['user']=request.user
        form = CreateTaskForm(instance_query,instance = obj)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect("tasks")
    context = {"form":form,'page':2}
    return render(request,'dashboard\ztasks.html',context)

@login_required(login_url="login")
def tasks(request):
    task = Tasks.objects.filter(user=request.user)
    context = {'tasks':task,'page':1}
    return render(request,"dashboard\ztasks.html",context)

@login_required(login_url="login")
def addTask(request):
    form = CreateTaskForm()
    if request.method == "POST":
        instance_query = request.POST.copy()
        instance_query['user']=request.user
        form = CreateTaskForm(instance_query)
        if form.is_valid():
            form.save()
            return redirect("tasks")
    context = {"form":form,'page':2}
    return render(request,'dashboard\ztasks.html',context)
    
@login_required(login_url="login")
def settings(request):
    return render(request,"dashboard\settings.html")

@login_required(login_url="login")
def analytics(request):
    return render(request,"dashboard\zanalytics.html")


