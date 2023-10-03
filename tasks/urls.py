from django.urls import path
from .import views

urlpatterns = [
    
    path('ola',views.tasks),
    
    path('lista/',views.taskList,name='task-list'),
    path('user',views.user,name='task-user'),
    path('curso/',views.cursoMeu,name='curso'),
    path('cadastro/',views.cadastro,name='cadastro-denuncia'), # type: ignore
    path('tasks/<int:id>',views.taskView,name="task-view"),
    path('',views.base,name="task-base"),
]
