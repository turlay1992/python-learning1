age: int = 25
price: float = 19.99
name: str = "Roman"
is_active: bool = True
nothing: None = None


5 // 2        # 2 — цілочисельне ділення (floor division), в JS такого немає
5 % 2         # 1 — остача, як у JS
5 ** 2        # 25 — степінь, в JS це **
5 == 5        # True — немає різниці == vs === , в Python == вже строгий за типом+значенням
not True      # False — замість !
True and False   # оператори and/or/not замість &&/||/!


score = 85
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"


for i in range(5):        # 0,1,2,3,4 — аналог Array.from({length:5})
    print(i)

for item in ["a", "b", "c"]:   # аналог for...of
    print(item)


n = 5
while n > 0:
    n -= 1     # немає n-- у Python!


def http_status(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:
            return "Server Error"
        case _:
            return "Unknown"
        

name = "Roman"
age = 30
print(f"{name} має {age} років")           # як `${name} має ${age} років`
print(f"{age * 2}")                        # вирази прямо всередині
print(f"{3.14159:.2f}")                    # 3.14 — format spec: 2 знаки після коми


# list — впорядкований, змінний (mutable), дозволяє дублікати. Прямий аналог JS
fruits: list[str] = ["apple", "banana", "cherry"]

# tuple — впорядкований, незмінний (immut). Повернуться n значень в визначеному порядку
point: tuple[int, int] = (10, 20)

# dict — асоціативний масив, ключ-значення, впорядкований.
user: dict[str, str | int] = {"name": "Roman", "age": 30}

# set — унікальні елементи, без порядку, без дублікатів. 
tags: set[str] = {"python", "backend", "python"}   # дублікат "python" ігнорується
a = {1, 2, 3}
b = {2, 3, 4}
a & b   # {2, 3} — перетин
a | b   # {1,2,3,4} — об'єднання
a - b   # {1} — різниця
{1, 2} ^ {1, 3} # {2,3} — {...}.symmetric.difference({...})
# короткий запис вимагає МНОЖИНИ З ОБОХ СТОРІН, через метод можна iterable