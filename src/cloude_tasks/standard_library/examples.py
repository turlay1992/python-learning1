# pathlib — робота з шляхами файлів.
from pathlib import Path

p = Path("data") / "users.json"     # `/` тут — оператор об'єднання шляхів, не ділення!
p.exists()                           # чи існує файл
p.read_text(encoding="utf-8")        # прочитати як текст
p.write_text("hello", encoding="utf-8")
p.parent                             # батьківська директорія
p.suffix                             # ".json"
list(Path(".").glob("*.py"))         # всі .py файли в поточній директорії


# os / sys — системні операції та інтерпретатор:
import os
import sys

os.environ.get("HOME")        # змінні середовища, аналог process.env в Node
os.getcwd()                    # поточна робоча директорія

sys.argv                       # аргументи командного рядка, аналог process.argv
sys.exit(1)                    # завершити скрипт з кодом помилки

# pathlib покриває більшість роботи з файлами/шляхами, 
# os/sys — для середовища й системних деталей.


# json — серіалізація, ідентична за духом до JSON.parse/JSON.stringify:
import json

data = {"name": "Roman", "age": 30}
json_str = json.dumps(data)              # у JSON-рядок, аналог JSON.stringify
json.dumps(data, indent=2)                # з відступами, для читабельності

parsed = json.loads(json_str)             # з JSON-рядка, аналог JSON.parse

with open("data.json", "w") as f:
    json.dump(data, f)                    # прямо у файл
    
    

# datetime / zoneinfo — робота з датами, аналог Date в JS (набагато зручніший):
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

now = datetime.now()                          # поточний час (naive, без таймзони)
now_kyiv = datetime.now(ZoneInfo("Europe/Kyiv"))   # з таймзоною — аналог Intl.DateTimeFormat

tomorrow = now + timedelta(days=1)             # арифметика з датами напряму
now.strftime("%Y-%m-%d")                       # форматування, аналог toLocaleDateString
datetime.fromisoformat("2026-08-03")           # парсинг ISO-рядка



# functools — функціональні утиліти:
from functools import lru_cache, reduce, partial

@lru_cache(maxsize=None)          # кешування результатів функції (мемоізація)
def fib(n: int) -> int:
    return n if n < 2 else fib(n-1) + fib(n-2)

print(fib(6))  # 8 

reduce(lambda a, b: a + b, [1, 2, 3, 4])   # аналог Array.reduce — 10

double = partial(lambda a, b, c: a * b + c, 2)          # часткове застосування аргументів
double(5, 3)   # 2 * 5 + 3 = 13 


# itertools — ефективна робота з ітераторами (ліниві обчислення, без створення проміжних списків):
from itertools import chain, product, groupby

list(chain([1, 2], [3, 4]))          # [1,2,3,4] — об'єднання, аналог [...a, ...b]
list(product([1, 2], ["a", "b"]))    # [(1,'a'),(1,'b'),(2,'a'),(2,'b')] — декартів добуток



# collections — спеціалізовані структури даних, які ти вже частково бачив (Counter):
from collections import Counter, defaultdict, namedtuple

Counter(["a", "b", "a", "c", "a"])         # Counter({'a': 3, 'b': 1, 'c': 1})

d = defaultdict(list)                       # dict, що автоматично створює дефолтне значення
d["fruits"].append("apple")                 # не треба перевіряти "чи є ключ" заздалегідь

Point = namedtuple("Point", ["x", "y"])     # легкий immutable-клас без писання __init__
p = Point(1, 2)
p.x, p.y   # 1, 2