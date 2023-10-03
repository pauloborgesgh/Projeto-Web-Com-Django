from os import name
from django.shortcuts import redirect, render ,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse

# Create your views here.
def tasks(request):
    return HttpResponse('olá')

def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    
    return render(request,'tasks/lista.html',{'tasks':tasks})

def taskView(request, id):
    
    task = get_object_or_404(Task, pk=id)
    return render (request, 'tasks/descricao.html',{'task':task}) 


def user(request):
    return render (request,'tasks/user.html')

def cursoMeu(request):
    
    return render(request,'tasks/curso.html')

def cadastro(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            print('salvou')
            return redirect('/')
        
        
    else:
        form = TaskForm()
        print('n validou')
    return render (request,'tasks/cadastro.html',{'form':form})
    
    
    
    
    
    
    
    

def base(request):
    return render (request,'tasks/base.html')


