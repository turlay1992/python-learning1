# 1
def revert_words(text: str) -> str:
    """Reverting words and store order

    Args:
        value (str): input text

    Returns:
        str: text with reverted words
    """
    
    words: list[str] = text.strip().split()
    reverted_words: list[str] = []
    for word in words:
        # word.reverse()
        reverted_words.append(word[::-1])
    return ' '.join(reverted_words)

    
print(revert_words('Hello world!'))


# 2
def is_palendrom(text: str) -> bool:
    """Check is text palendrome

    Args:
        text (str): input text

    Returns:
        bool: is text palendrome"""
    prepared_text: str = "".join(text.strip().lower().split())
    reversed_text: str = prepared_text[::-1]
    return prepared_text == reversed_text


print(is_palendrom('123 123'))
print(is_palendrom('12   1  121'))


# 3
def get_count_of_inputs(text: str, searched_chars: list[str]=['а', 'о', 'у', 'е', 'и', 'і']) -> int:
    """Return count of inputs of searched_chars in text

    Args:
        text (str): input text
        [searched_chars] (list[str]): chars for searching

    Returns:
        int: count of inputs of searched_chars"""
    count: int = 0
    for char in searched_chars:
        count += text.count(char)
    
    return count
        
print(get_count_of_inputs('Підрахунок голосних букв у рядку.'))


# 4
def capitalize_words(text: str) -> str:
    """Capotalize each word in text

    Args:
        text (str): input text

    Returns:
        str: String with capitalized words
    """
    words: list[str] = text.strip().split()
    capitalized_words = [word.capitalize() for word in words]
    
    return ' '.join(capitalized_words)

print(capitalize_words('Зробити кожне слово в реченні з великої букви — без використання str.title()'))


# 5
def increse_price_on_percent(items: dict[str, float], percent: int = 10) -> dict[str, float]:
    """Return item with increased value on percent"""
    copy_items = items.copy()
    for title, price in copy_items.items():
        copy_items[title] = round(price + price * (percent / 100), 2)
        
    return copy_items

print(increse_price_on_percent(
    {
        'Item 1': 25,
        'Item 2': 75
    }
))

# 6
def invert_key_value(original: dict[str, int]) -> dict[int, list[str]]:
    """Return dict with inverter key-value"""
    inverted: dict[int, list[str]] = {}

    for key, value in original.items():
        inverted.setdefault(value, []).append(key)
    
    return inverted
    
print(invert_key_value(
    {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
))


# 7
from typing import TypeAlias, TypedDict
class UserItem(TypedDict):
    name: str
    age: int
Item_7_type: TypeAlias = list[UserItem]

def group_users_by_age10(original: Item_7_type) -> dict[int, list[str]]:
    """Return groups of users drouped by (age // 10) * 10"""
    groups: dict[int, list[str]] = {}
    
    for user_dict in original:
        name = user_dict["name"]
        age = user_dict["age"]
        group_name: int = (age // 10) * 10
        groups.setdefault(group_name, []).append(name)
        
    return groups
        
print(group_users_by_age10(
    [
        {"name": "Олексій", "age": 30},
        {"name": "Марія", "age": 25},
        {"name": "Mepi", "age": 28},
        {"name": "Оксана", "age": 47},
        {"name": "Олег", "age": 13}
    ]
))


# 8
def join_dicts_and_sum_by_key(*dicts: dict[str, int]) -> dict[str, int]:
    """Return new dict with sum of values if same key"""
    
    result: dict[str, int] = {}
    for d in dicts:
        for name, age in d.items():
            result[name] = result.get(name, 0) + age
    
    return result

print(join_dicts_and_sum_by_key(
    {"Олексій": 30},
    {"Марія": 25},
    {"Mepi": 28},
    {"Оксана": 47},
    {"Олег": 13},
    {"Олексій": 13}
))

# 9
from pathlib import Path
from itertools import zip_longest

def parse_CSV_to_dict(path: Path) -> list[dict[str, list[str]]]:
    """Parse CSV file and return sets by keys"""
    
    result: list[dict[str, list[str]]] = []
    csv_keys: list[str] = []
    csv_values: list[list[str]] = []
    with open(path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            line_list: list[str] = line.strip().split(',')
            
            if line_num == 1:
                csv_keys = line_list
            else:
                csv_values.append(line_list)
    for key, *values in zip_longest(csv_keys, *csv_values, fillvalue=''):
        result.append({key: values})
    
    return result

BASE_DIR: Path = Path.cwd()
LOG_FILE: Path = BASE_DIR / 'src' / 'cloude_tasks' / 'block1_practice' / 'test_users.csv'
print(parse_CSV_to_dict(LOG_FILE))

# 11
from pathlib import Path
def find_word_in_file(path: Path, search_term: str) -> list[dict[int, str]]:
    """Parse CSV file and return line numbers and line texts"""
    
    result: list[dict[int, str]] = []
    with open(path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, start=1):
                if search_term in line:
                    result.append({line_num: line.strip()})
    
    
    return result

BASE_DIR1: Path = Path.cwd()
LOG_FILE1: Path = BASE_DIR1 / 'src' / 'cloude_tasks' / 'block1_practice' / 'test_users.csv'
print(find_word_in_file(LOG_FILE1, 'Київ'))


# 12

class Rectangle:
    """Simple calculation of area and square for rectangle"""
    
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height
        
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return (self.width + self.height) * 2
        
    @classmethod
    def square(cls, width: float) -> 'Rectangle':
        return cls(width, width)
    
rect1: Rectangle = Rectangle(12, 34)
print(f'Rect area: {rect1.area()}, Rect perimeter: {rect1.perimeter()}')

square: Rectangle = Rectangle.square(13)
print(f'Square area: {square.area()}, Square perimeter: {square.perimeter()}')
