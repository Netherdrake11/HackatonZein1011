from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    user_count = User.objects.count()
    return render(request,'main/index.html',{'user_count': user_count})

def about(request):
    return render(request,'main/about.html')

def words1(request):
    return render(request,'main/words.html')


from django.shortcuts import render, redirect
from .models import Word
from .forms import WordForm

from django.shortcuts import render
from .models import Word

def words2(request):
    words = Word.objects.all()  # Получаем все слова из базы данных
    context = {'words': words}  # Передаем их в шаблон
    return render(request, 'main/words.html', context)


from django.shortcuts import render
from .models import Word


def words3(request):
    search_query = request.GET.get('search', '')  # Получаем параметр поиска
    if search_query:
        # Если есть запрос, фильтруем слова по совпадению с введенным словом
        words = Word.objects.filter(word__icontains=search_query)
    else:
        # Если поиска нет, выводим все слова
        words = Word.objects.all()

    context = {'words': words}
    return render(request, 'main/words.html', context)


from django.db.models import Q
from django.shortcuts import render
from .models import Word


def words(request):
    search_query = request.GET.get('search', '')  # Получаем параметр поиска
    if search_query:
        # Фильтрация по основному слову и переводу
        words = Word.objects.filter(
            Q(word__icontains=search_query) | Q(translation__icontains=search_query)
        )
    else:
        # Если поиска нет, выводим все слова
        words = Word.objects.all()

    context = {'words': words}
    return render(request, 'main/words.html', context)



from django.shortcuts import render, redirect
from .models import Lesson
from .forms import LessonForm

def lessons(request):
    lessons = Lesson.objects.all()
    return render(request, 'main/about.html', {'lessons': lessons})

def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lessons')
    else:
        form = LessonForm()
    return render(request, 'main/add_lessons.html', {'form': form})


from django.shortcuts import render

def testmain(request):
    return render(request, 'main/testmain.html')

def tasks(request):
    return render(request, 'main/tasks.html')



# # Страница с уровнями
# def lessons(request):
#     levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']  # Уровни
#     return render(request, 'main/lessons.html', {'levels': levels})
#
# # Страница для конкретного уровня
# def level_lessons(request, level):
#     lessons = {
#         'A1': ['Lesson 1', 'Lesson 2', 'Lesson 3'],
#         'A2': ['Lesson 1', 'Lesson 2', 'Lesson 3'],
#         'B1': ['Lesson 1', 'Lesson 2', 'Lesson 3'],
#         'B2': ['Lesson 1', 'Lesson 2', 'Lesson 3'],
#         'C1': ['Lesson 1', 'Lesson 2', 'Lesson 3'],
#         'C2': ['Lesson 1', 'Lesson 2', 'Lesson 3'],
#     }
#     level_lessons = lessons.get(level, [])
#     return render(request, 'main/level_lessons.html', {'level': level, 'lessons': level_lessons})
#


from django.shortcuts import render, get_object_or_404
from .models import Level, Lesson

def level_list(request):
    levels = Level.objects.all()
    return render(request, 'main/level_list.html', {'levels': levels})

def lesson_list(request, level_id):
    level = get_object_or_404(Level, pk=level_id)
    lessons = level.lessons.all()
    return render(request, 'main/lesson_list.html', {'level': level, 'lessons': lessons})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'main/lesson_detail.html', {'lesson': lesson})


from django.shortcuts import render, redirect
from .forms import InteractiveTaskForm
from .models import InteractiveTask

def add_task(request):
    if request.method == 'POST':
        form = InteractiveTaskForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базе
            return redirect('task_list')  # Перенаправляем на страницу со списком заданий
    else:
        form = InteractiveTaskForm()
    return render(request, 'main/add_task.html', {'form': form})

def task_list(request):
    tasks = InteractiveTask.objects.all()  # Получаем все задания
    return render(request, 'main/task_list.html', {'tasks': tasks})



from .models import TestQuestion
from .forms import TestForm


def test_view(request):
    if request.method == 'POST':
        # Если данные отправлены, проверяем ответы
        form = TestForm(request.POST)
        if form.is_valid():
            correct_answers = 0
            total_questions = TestQuestion.objects.count()
            questions = TestQuestion.objects.all()

            # Подсчёт правильных ответов
            for i, question in enumerate(questions):
                user_answer = form.cleaned_data.get(f'question_{i}')
                if user_answer.lower() == question.correct_answer.lower():
                    correct_answers += 1

            # Рассчитываем процент правильных ответов
            percentage = (correct_answers / total_questions) * 100
            return render(request, 'main/test_result.html', {'percentage': percentage, 'correct_answers': correct_answers,
                                                        'total_questions': total_questions})

    else:
        # Если GET-запрос, создаём форму с вопросами
        form = TestForm()

    return render(request, 'main/test_page.html', {'form': form})
