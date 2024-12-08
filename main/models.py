from django.db import models

# Create your models here.
from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=100, unique=True)  # Слово
    translation = models.CharField(max_length=255)       # Перевод

    def __str__(self):
        return self.word

# from django.db import models

# class Lesson(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Название урока")
#     description = models.TextField(blank=True, verbose_name="Описание урока")
#     video = models.FileField(upload_to='lessons/videos/', blank=True, null=True, verbose_name="Видео материал")
#     audio = models.FileField(upload_to='lessons/audios/', blank=True, null=True, verbose_name="Аудио материал")
#     image = models.ImageField(upload_to='lessons/images/', blank=True, null=True, verbose_name="Изображение")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
#
#     def __str__(self):
#         return self.title


from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название уровня")

    def _str_(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название урока")
    description = models.TextField(verbose_name="Краткое содержание")
    video = models.FileField(upload_to='videos/', blank=True, null=True, verbose_name="Видео")
    audio = models.FileField(upload_to='audios/', blank=True, null=True, verbose_name="Аудио")
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="Изображение")
    test_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на тест")
    additional_links = models.TextField(blank=True, null=True, verbose_name="Дополнительные материалы (ссылки)")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="lessons", verbose_name="Уровень")

    def _str_(self):
        return self.title

from django.db import models

class InteractiveTask(models.Model):
    LEVELS = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    ]
    level = models.CharField(max_length=2, choices=LEVELS, default='A1')  # Уровень задания
    question = models.TextField()  # Вопрос задания
    answer = models.CharField(max_length=255)  # Ответ на задание

    def __str__(self):
        return f"{self.level} - {self.question[:50]}..."


class TestQuestion(models.Model):
    question = models.CharField(max_length=255)  # Вопрос
    correct_answer = models.CharField(max_length=255)  # Правильный ответ

    def __str__(self):
        return self.question