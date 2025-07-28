"""
!/usr/bin/env python3

Rich Demo: Полное руководство с примерами
-----------------------------------------
Этот файл демонстрирует основные возможности библиотеки Rich для Python.
Каждый раздел содержит подробное описание и рабочий пример.

Требования:
   pip install rich
"""

# Импорт необходимых модулей
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, track
from rich.tree import Tree
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.json import JSON
from rich.panel import Panel
from rich.layout import Layout
import time
import json
import csv
import random

# Инициализация консоли для вывода
console = Console()

# Демонстрация базовых стилей Rich
def demo_basic_styles():
   """
   Демонстрация базовых стилей:
   - Цветной текст
   - Разные стили (жирный, курсив)
   - Эмодзи
   - Горизонтальные линии
   """
   # Создание горизонтального разделителя с заголовком
   console.rule("[bold red]1. Базовые стили Rich")
   
   # Простое форматирование текста
   console.print("Это [bold green]жирный зеленый[/] текст!")
   console.print("Это [italic yellow]желтый курсив[/] :)")
   
   # Использование эмодзи
   console.print("Эмодзи поддерживаются! :thumbs_up: :rocket: :snake:", style="bold blue")
   
   # Горизонтальный разделитель без текста
   console.rule()

# Демонстрация таблиц
def demo_tables():
   """
   Создание форматированных таблиц:
   - Заголовки со стилями
   - Разные выравнивания
   - Многострочные ячейки
   - Кастомизация внешнего вида
   """
   # Заголовок раздела
   console.rule("[bold blue]2. Таблицы")

   # Создание таблицы с заголовком
   table = Table(title="Фильмы 2023 года", show_header=True, header_style="bold magenta")
   
   # Добавление колонок с настройками
   table.add_column("Название", style="cyan", width=20)
   table.add_column("Жанр", justify="center")
   table.add_column("Рейтинг", justify="right")
   table.add_column("Бюджет", justify="right")
   
   # Добавление строк данных
   table.add_row("Оппенгеймер", "Биография/Драма", "8.6", "$100M")
   table.add_row("Барби", "Комедия/Фэнтези", "7.0", "$145M")
   table.add_row(
       "Крушение\n(про инцидент с Boeing)", 
       "Триллер/Драма", 
       "7.7", 
       "$30M",
       style="on grey15"  # Специальный стиль для строки
   )
   
   # Вывод таблицы в консоль
   console.print(table)

# Демонстрация прогресс-баров
def demo_progress_bars():
   """
   Прогресс-бары:
   - Простой прогресс-бар с track()
   - Множественные прогресс-бары
   - Интеграция с реальными задачами
   """
   console.rule("[bold green]3. Прогресс-бары")
   
   # Простой прогресс-бар
   console.print("Простой прогресс-бар:")
   for _ in track(range(20), description="Обработка..."):
       time.sleep(0.05)  # Имитация работы
   
   # Множественные прогресс-бары
   console.print("\nМножественные прогресс-бары:")
   with Progress() as progress:
       # Создание двух задач
       task1 = progress.add_task("[red]Скачивание...", total=100)
       task2 = progress.add_task("[green]Обработка...", total=80)
       
       # Обновление прогресса
       while not progress.finished:
           progress.update(task1, advance=0.9)
           progress.update(task2, advance=0.5)
           time.sleep(0.02)

# Демонстрация древовидных структур
def demo_tree_view():
   """
   Визуализация иерархических данных:
   - Древовидные структуры
   - Кастомизация стилей
   - Динамическое построение
   """
   console.rule("[bold yellow]4. Древовидные структуры")
   
   # Создание корневого элемента дерева
   tree = Tree("📁 Проект Python", guide_style="bold bright_blue")
   
   # Добавление основных веток
   src = tree.add("📁 src", style="bold green")
   src.add("main.py")
   src.add("utils.py")
   
   tests = tree.add("📁 tests", style="bold red")
   tests.add("test_main.py")
   tests.add("test_utils.py")
   
   docs = tree.add("📁 docs", style="bold cyan")
   docs.add("README.md")
   docs.add("[italic]tutorial.md")
   
   # Вложенные структуры
   config = tree.add("⚙️ Конфигурация")
   config.add("settings.toml")
   config.add(".env")
   
   # Вывод дерева
   console.print(tree)

# Демонстрация рендеринга Markdown
def demo_markdown():
   """
   Рендеринг Markdown в консоли:
   - Заголовки
   - Списки
   - Код
   - Цитаты
   """
   console.rule("[bold purple]5. Markdown Рендеринг")
   
   # Содержимое Markdown
   md_content = """
# Заголовок 1
## Заголовок 2

- **Жирный элемент списка**
- *Курсив*
- `Код в строке`

```python
## Блок кода
def hello():
   print("Hello, Rich!")
```

> Цитата: Используйте Rich для красивых консолей!
   """
   
   # Рендеринг и вывод Markdown
   console.print(Markdown(md_content))

# Демонстрация подсветки синтаксиса
def demo_syntax_highlighting():
   """
   Подсветка синтаксиса для кода:
   - Выбор языка
   - Темы оформления
   - Номера строк
   """
   console.rule("[bold cyan]6. Подсветка синтаксиса")
   
   # Пример кода Python
   code = '''
def factorial(n):
   """Вычисляет факториал"""
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
'''
   # Создание блока кода с подсветкой
   syntax = Syntax(
       code, 
       "python", 
       theme="monokai", 
       line_numbers=True,
       word_wrap=True
   )
   
   # Вывод в панели
   console.print(Panel(syntax, title="Пример кода Python", subtitle="theme: monokai"))

# Демонстрация работы с JSON
def demo_json_handling():
   """
   Работа с JSON:
   - Красивый вывод
   - Подсветка синтаксиса
   - Обработка ошибок
   """
   console.rule("[bold magenta]7. JSON Обработка")
   
   # Пример JSON-данных
   json_data = {
       "project": "Rich Demo",
       "author": "Ваше Имя",
       "tags": ["python", "cli", "ui"],
       "metadata": {
           "version": "1.0",
           "created": "2023-10-15"
       }
   }
   
   # Конвертация в строку
   json_str = json.dumps(json_data, indent=2)
   
   # Красивый вывод JSON
   console.print(JSON(json_str))

# Демонстрация работы с CSV
def demo_csv_tables():
   """
   Преобразование CSV в таблицы:
   - Автоматическое форматирование
   - Заголовки столбцов
   - Кастомизация отображения
   """
   console.rule("[bold orange]8. CSV в Таблицы")
   
   # CSV данные в виде строки
   csv_data = """Name,Age,Occupation,Salary
Иван Петров,35,Инженер,120000
Мария Сидорова,28,Дизайнер,95000
Алексей Иванов,42,Менеджер,150000"""
   
   # Чтение CSV
   reader = csv.DictReader(csv_data.splitlines())
   
   # Создание таблицы
   table = Table(title="Сотрудники", show_header=True, header_style="bold blue")
   for header in reader.fieldnames:
       table.add_column(header)
   
   # Добавление строк
   for row in reader:
       table.add_row(*row.values())
   
   # Вывод таблицы
   console.print(table)

# Демонстрация системы макетов
def demo_layout_system():
   """
   Система макетов для сложных интерфейсов:
   - Разделение экрана на части
   - Разные панели
   - Динамическое обновление
   """
   console.rule("[bold red]9. Система Макетов")
   
   # Создание макета
   layout = Layout()
   
   # Разделение на вертикальные части
   layout.split_column(
       Layout(name="header", size=3),
       Layout(name="main", ratio=2),
       Layout(name="footer", size=3)
   )
   
   # Заполнение разделов
   layout["header"].update(Panel("Демонстрация системы макетов Rich", style="on blue"))
   layout["main"].update(Panel("Основной контент\nМожно добавлять любые Rich-объекты", style="bright_white on grey15"))
   layout["footer"].update(Panel("Статус: [green]Готово[/]", style="on yellow"))
   
   # Вывод макета
   console.print(layout)

# Демонстрация live-мониторинга
def demo_live_monitoring():
   """
   Имитация live-мониторинга:
   - Динамическое обновление консоли
   - Цветовая индикация статуса
   - Анимация
   """
   console.rule("[bold green]10. Live-Мониторинг")
   
   # Статус бар с анимацией
   with console.status("[bold green]Мониторинг системы...", spinner="dots"):
       for i in range(10):
           time.sleep(0.5)
           # Случайный выбор цвета для события
           color = "green" if random.random() > 0.3 else "red"
           console.log(f"Событие #{i+1}: [{color}]Завершено")
   
   console.print("✅ [bold green]Мониторинг завершен")

# Главная функция
if __name__ == "__main__":
   # Очистка консоли
   console.clear()
   
   # Центрированный заголовок
   console.rule("[bold blue] 🚀 Rich Library Demo ", align="center")
   
   # Запуск всех демонстраций
   demo_basic_styles()

   # Рекламная пауза на 3 секунды для понимания происходящего
   time.sleep(3)

   demo_tables()

   # Рекламная пауза на 3 секунды для понимания происходящего
   time.sleep(3)
   
   demo_progress_bars()
   
   # Рекламная пауза на 3 секунды для понимания происходящего
   time.sleep(3)
   
   demo_tree_view()
   
   # Рекламная пауза на 3 секунды для понимания происходящего
   time.sleep(3)
   
   demo_markdown()
   
   # Рекламная пауза на 3 секунды для понимания происходящего
   time.sleep(3)

   demo_syntax_highlighting()
   
   # Рекламная пауза на 3 секунды для понимания происходящего
   time.sleep(3)

   demo_json_handling()
   
   # Рекламная пауза на 3 секунды для понимания происходящего
   time.sleep(3)

   demo_csv_tables()
   
   # Рекламная пауза на 3 секунды для понимания происходящего
   time.sleep(3)

   demo_layout_system()
   
   # Рекламная пауза на 3 секунды для понимания происходящего
   time.sleep(3)
   
   demo_live_monitoring()
   
   # Завершающий разделитель
   console.rule("[bold green] Демонстрация завершена ")
