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

def parse_CSV_to_dict(path: Path) -> list[dict[str, list[str]]]:
    """Parse CSV file and return sets by keys"""
    
    result: list[dict[str, list[str]]] = []
    csv_keys: list[str] = []
    values: list[list[str]] = []
    with open(path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            line_list: list[str] = line.strip().split(',')
            
            if line_num == 1:
                csv_keys = line_list
            else:
                values.append(line_list)
    return result
        