from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Word

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'translation')  # Отображение столбцов в админке
    search_fields = ('word',)  # Поиск по слову

# from django.contrib import admin
# from .models import Lesson
#
# @admin.register(Lesson)
# class LessonAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#     search_fields = ('title',)

from django.contrib import admin
from .models import Level, Lesson

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'level')
    list_filter = ('level',)