from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'translation']
        labels = {
            'word': 'Слово',
            'translation': 'Перевод'
        }

from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'video', 'audio', 'image']


from django import forms
from .models import InteractiveTask

class InteractiveTaskForm(forms.ModelForm):
    class Meta:
        model = InteractiveTask
        fields = ['level', 'question', 'answer']
        widgets = {
            'level': forms.Select(attrs={'class': 'form-control'}),
            'question': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'answer': forms.TextInput(attrs={'class': 'form-control'}),
        }

from .models import TestQuestion

class TestForm(forms.Form):
    # Создаём форму для вопросов. Каждый вопрос будет иметь свой текст и поле для ввода ответа
    def __init__(self, *args, **kwargs):
        # Инициализация формы с динамическими вопросами
        super().__init__(*args, **kwargs)
        questions = TestQuestion.objects.all()
        for i, question in enumerate(questions):
            self.fields[f'question_{i}'] = forms.CharField(
                label=question.question,
                widget=forms.TextInput(attrs={'placeholder': 'Введите ответ'}),
                required=True
            )