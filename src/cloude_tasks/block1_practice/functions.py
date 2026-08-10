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