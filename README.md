bash
  python -m venv .venv        # створити ізольоване середовище в папці .venv
  source .venv/bin/activate   # активувати (Linux/Mac)
  # .venv\Scripts\activate    # активувати (Windows)
  pip install requests        # ставиться ЛИШЕ всередині .venv, не глобально

Після активації pip та python в терміналі вказують на версії всередині .venv, а не на системний Python. Це найближчий аналог до того, що node_modules + package.json роблять автоматично в Node — тільки в Python це явний, ручний крок.

.venv не комітиться в git (як і node_modules) — комітиться лише список залежностей (requirements.txt або pyproject.toml — аналог package.json).



Що означає цей рядок? Що таке тут "Scripts\activate" - # .venv\Scripts\activate


Це той самий крок активації venv, тільки шлях відрізняється між ОС через різну структуру папок:

Linux/Mac: виконувані файли лежать у .venv/bin/, тому активація — source .venv/bin/activate
Windows: виконувані файли лежать у .venv\Scripts\, тому активація — .venv\Scripts\activate (у PowerShell: .venv\Scripts\Activate.ps1)

activate — це не програма, а shell-скрипт, який треба виконати в поточному терміналі (не запустити окремим процесом). Він міняє змінні середовища поточної сесії терміналу, зокрема:

PATH — додає .venv\Scripts (або .venv/bin) на початок, тому команда python тепер знаходить інтерпретатор з .venv, а не системний
Змінює промпт терміналу — зазвичай додає (.venv) на початку рядка, щоб було видно, що середовище активне

Після активації pip install і python script.py працюють у межах цього ізольованого середовища. Деактивація — просто команда deactivate.

Оскільки ти на Windows — використовуй саме .venv\Scripts\activate 

Install dependencies from .toml file
python -m pip install -e .

pip install mypy
mypy --strict fizzbuzz.py

pip install tzdata
OR
python -m pip install tzdata