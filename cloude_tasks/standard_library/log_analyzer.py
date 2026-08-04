# Практичне завдання: напиши скрипт log_analyzer.py, який:

# Створює (через pathlib) невеликий текстовий файл events.log з кількома рядками формату 
# 2026-08-01 ERROR Connection failed / 2026-08-01 INFO User logged in 
# (сам придумай 8-10 рядків з рівнями INFO/WARNING/ERROR)
# Читає файл, парсить кожен рядок (дата, рівень, повідомлення)
# Використовуючи Counter, рахує скільки разів зустрічається кожен рівень (INFO/WARNING/ERROR)
# Зберігає результат підрахунку у summary.json через json.dump
# Виводить поточну дату й час створення звіту через datetime.now()

from pathlib import Path

log_file_name: str = 'events.log' 
log_file = Path('cloude_tasks' / 'cloude_tasks' / 'standard_library') / log_file_name
#cloude_tasks\standard_library\log_analyzer.py

if log_file.exists():
    print('File already exist')
else:
    log_file.touch() # Створює пустий файл, якщо його ще немає