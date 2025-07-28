import platform
import sys
from datetime import datetime

# ANSI цветовые коды
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BG_BLUE = "\033[44m"
BG_YELLOW = "\033[43m"

# Сбор информации
system_info = {
    "Операционная система": platform.system(),
    "Название ОС": platform.platform(),
    "Версия ОС": platform.version(),
    "Архитектура": platform.architecture()[0],
    "Процессор": platform.processor() or "Не определён",
    "Имя компьютера": platform.node(),
    "Версия Python": platform.python_version(),
    "Компилятор": platform.python_compiler(),
    "Сборка Python": platform.python_build()[0],
    "Реализация Python": platform.python_implementation(),
    "Платформа": sys.platform
}

# Вывод с оформлением
print(f"\n{BG_BLUE}{BOLD}{' СИСТЕМНАЯ ИНФОРМАЦИЯ ':=^60}{RESET}")
for i, (param, value) in enumerate(system_info.items()):
    color = YELLOW if i % 2 == 0 else CYAN
    print(f"{BOLD}{GREEN}• {param}:{RESET} {color}{value}{RESET}")

print(f"\n{BOLD}{MAGENTA}Сформировано:{RESET} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")