from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),
    path('taskList/', views.taskList, name='taskList'),
    path('tasks_per_day_view/', views.tasks_per_day_view, name='tasks_per_day_view'),
    path('tasks_graph/', views.tasks_graph, name='tasks_graph'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

