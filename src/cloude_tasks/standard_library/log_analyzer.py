# Практичне завдання: напиши скрипт log_analyzer.py, який:

# Створює (через pathlib) невеликий текстовий файл events.log з кількома рядками формату 
# 2026-08-01 ERROR Connection failed / 2026-08-01 INFO User logged in 
# (сам придумай 8-10 рядків з рівнями INFO/WARNING/ERROR)
# Читає файл, парсить кожен рядок (дата, рівень, повідомлення)
# Використовуючи Counter, рахує скільки разів зустрічається кожен рівень (INFO/WARNING/ERROR)
# Зберігає результат підрахунку у summary.json через json.dump
# Виводить поточну дату й час створення звіту через datetime.now()

from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo


BASE_DIR: Path = Path.cwd()
LOG_DIR: Path = BASE_DIR / 'src' / 'cloude_tasks'  / 'standard_library'
# LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE: Path = LOG_DIR / 'events.log' 
LOG_FILE_BACKUP: Path = LOG_DIR / 'events_backup.log' 

now_kyiv: datetime = datetime.now(ZoneInfo("Europe/Kyiv"))


if LOG_FILE.exists():
    print('LOG_FILE already exist')
else:
    LOG_FILE.touch() # Створює пустий файл, якщо його ще немає
    
    
logs: list[str] = [
    "2026-08-01 ERROR Connection failed",
    "2026-08-01 INFO User logged in",
    "2026-08-01 WARNING Disk usage 85%",
    "2026-08-01 ERROR Database timeout",
    "2026-08-02 INFO Backup started",
    "2026-08-02 INFO Backup finished",
    "2026-08-02 ERROR Connection failed",
    "2026-08-03 INFO User logged out",
    "2026-08-03 WARNING CPU temperature high",
    "2026-08-03 ERROR Invalid password",
]

with open(LOG_FILE, 'w', encoding='utf-8') as file:
    for log in logs:
        file.write(log + '\n')
        

with open(LOG_FILE, "rb") as src, open(LOG_FILE_BACKUP, "wb") as dst:
    dst.write(src.read())


print(LOG_FILE.read_bytes() == LOG_FILE_BACKUP.read_bytes())
        

total = 0
levels: dict[str, int] = defaultdict(int)
dates: dict[str, int] = defaultdict(int)

        
with open(f'{LOG_FILE}', 'r', encoding='utf-8') as file:
    for line in file:
        date, level, message = line.strip().split(' ', maxsplit=2)
        total += 1
        levels[level] += 1
        dates[date] += 1
        

stats = {
    "total": total,
    "levels": levels,
    "dates": dates,
}
        
import json


SUMMARY_FILE: Path = LOG_DIR / 'summary.json'
if SUMMARY_FILE.exists():
    print('SUMMARY_FILE already exist')
else:
    SUMMARY_FILE.touch() # Створює пустий файл, якщо його ще немає
    
with open(SUMMARY_FILE, 'w', encoding='utf-8') as file:
    json.dump(
        {
            'created_at': str(now_kyiv),
            'stats': stats
        },
        file, 
        indent=4
    )



level_count: Counter[str] = Counter()
messages: defaultdict[str, list[str]] = defaultdict(list)

with open(LOG_FILE, 'r', encoding='utf-8') as file:
    for line in file:
        _, level, message = line.strip().split(' ', maxsplit=2)
        
        level_count[level] += 1
        messages[level].append(message)
        

SUMMARY_FILE_EXTENDED: Path = LOG_DIR / 'summary_extended.json'
if SUMMARY_FILE_EXTENDED.exists():
    print('SUMMARY_FILE_EXTENDED already exist')
else:
    SUMMARY_FILE_EXTENDED.touch() # Створює пустий файл, якщо його ще немає
    
with open(SUMMARY_FILE_EXTENDED, 'w', encoding='utf-8') as file:
    json.dump(
        {
            'created_at': str(now_kyiv),
            'level_count' : level_count, 
            'messages' : messages
        },
        file,
        indent=4
    )