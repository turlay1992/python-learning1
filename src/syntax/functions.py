# позиційні аргументи
def printing_positional_args(first: str, second: str) -> None:
    print(second, first, 'зміна позицій аргументів змінює порядок')
    print(first, second)


# if you have more then 2 atr
def sum_two_numbers(a: int, b: int, *args: int) -> int:
    return a + b + sum(args)

print(sum_two_numbers(1, 2, 3, 4, 5))
print(sum_two_numbers(1, 2, *range(10)))


# v2
def user_greetings(name: str, surname: str, *additional_information: str) -> str:
    return f"hello {name} {surname}\n your information is {additional_information}"  # але краще args

# ключові аргументи

def printing_positional_args2(first: str, second: str) -> None:
    print(f'{first=}, {second=}')


printing_positional_args2(first='First', second='Second')

def example_keyword(first: str | None = None, second: str = 'Second') -> tuple[str | None, str]:
    return first, second

print(example_keyword())

# можна комбінувати але позіційні перші
def example_keyword2(first: str, second: str | None = None, third: str = 'Second') -> tuple[str, str | None, str]:
    return first, second, third

print(example_keyword2('1'))

# а чи можна передати ключових більше ніж потрібно
def example_keyword3(first: str, second: int | None = None, third: str = 'Second', **kwargs: str) -> tuple[str, int | None, str, dict[str, str]]:
    for key, value in kwargs.items():
        print(f'{key=}, {value=}')
    
    return first, second, third, kwargs

print(example_keyword3('1', 2, "Third", a="a1", b="b1"))


def args(a: int,b: int,/,c: int,d: int,*,f: int,g: int) -> None:
    print(a,b,c,d,f,g)
    
args(1,2,3,4,f=5,g=6)

"""Positional-only і keyword-only маркери — цього немає прямого еквівалента в JS, 
і це специфічно для Python:"""

def f(a: int, b: int, /, c: int, d: int, *, e: int, f: int) -> int:
    return a + b + c + d + e + f
#        ^-------^  позиційні тільки       ^-------^ іменовані тільки
#          (до /)                            (після *)
#                  a, b, c, d - можна звичайно (позиційно чи іменовано, крім a,b)

# --------------------------------------------------------------
