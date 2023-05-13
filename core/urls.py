from django.urls import path
from .views import HomeTemplateView
from .views import task_list

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    # path("login", HomeTemplateView , name="login")
      path('tasks/', task_list, name='task_list'),
      path('/', task_list, name='task_list'),
      
]
