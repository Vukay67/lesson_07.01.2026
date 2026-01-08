from django.contrib import admin
from django.urls import path, re_path
from core.views import main_page, students_page, date_page, test_page, task, calculator

# URL Dispatcher (Диспетчер ссылок)
# Он решает совпадает ли текущая ссылка хоть с одним из path

# Динамические URL(ссылки)
# Типы данных:
# int, str, slug(тоже строка), uuid, path
# <тип_данных:название_переменной>/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name="main_page"),
    path('test/', test_page, name="test_page"), 
    path('students/<str:test>/', students_page, name="students_page"),
    path('calculator/', calculator, name="calculator_page"),
    path('task/', task),
    re_path(r'date/(?P<date>\d{2}-\d{2}-\d{4})/$', date_page, name="date_page"),
]
