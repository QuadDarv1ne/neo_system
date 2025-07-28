import platform
import sys
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box

# Сбор информации
system_info = {
    "🖥️  Операционная система": platform.system(),
    "📦  Название ОС": platform.platform(),
    "🔢  Версия ОС": platform.version(),
    "🧩  Архитектура": platform.architecture()[0],
    "⚙️  Процессор": platform.processor() or "Не определён",
    "🏷️  Имя компьютера": platform.node(),
    "🐍  Версия Python": platform.python_version(),
    "🔧  Компилятор": platform.python_compiler(),
    "🏗️  Сборка Python": platform.python_build()[0],
    "💡  Реализация Python": platform.python_implementation(),
    "🌐  Платформа": sys.platform
}

# Создание красивого вывода
console = Console()

table = Table(
    title="[bold cyan]Системная информация[/bold cyan]", 
    box=box.ROUNDED,
    header_style="bold magenta",
    show_header=False
)

table.add_column("Параметр", style="bold green", width=25)
table.add_column("Значение", style="yellow")

for param, value in system_info.items():
    table.add_row(param, value)

# Вывод результатов
console.print(table)
console.print(f"📅 [italic]Сформировано:[/italic] [bold]{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}[/bold]")