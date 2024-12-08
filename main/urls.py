from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('words/', views.words, name = 'words'),



    path('testmain/', views.testmain, name='testmain'),
    path('testmain/tasks/', views.tasks, name='tasks'),
    # path('testmain/lessons/', views.lessons, name='lessons'),  # Страница всех уровней
    # path('testmain/lessons/<str:level>/', views.level_lessons, name='levellessons'),
    path('levels/', views.level_list, name='level_list'),  # Страница выбора уровня
    path('levels/<int:level_id>/lessons/', views.lesson_list, name='lesson_list'),  # Уроки в уровне
    path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),

    path('testmain/tasks/', views.task_list, name='task_list'),  # Список заданий
    path('testmain/tasks/add/', views.add_task, name='add_task'),  # Добавление задания
    path('testmain/test/', views.test_view, name='test_view'),
]