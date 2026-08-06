count_of_iterations: int = 30


def get_division_result(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else: 
        return str(number)
    

for i in range(1, count_of_iterations + 1):
    print(f"{i}: {get_division_result(i)}")

# fruits: list[str] = ["apple", "banana", "cherry"]
# user: dict[str, str | int | list[str]] = {"name": "Roman", "age": 30, "eat": fruits}


# Work with collections-------------------------------------

fruits: list[str] = [
    "apple", "banana", "apple", "cherry", "banana",
    "apple", "date", "cherry", "apple", "banana",
]


def get_fruits_entry(fruits: list[str]) -> tuple[str, int]:
    fruits_set: set[str] = set(fruits)
    print(f'{fruits_set}')
    
    fruits_dict: dict[str, int] = {}
    for fruit in fruits_set:
        fruits_dict[fruit] = fruits.count(fruit)
        
    print(f'{fruits_dict}')
    
    # Error in --strict mode (get can return None)
    # max_entries_name: str = max(fruits_dict, key=fruits_dict.get) 
    max_entries_name: str = max(fruits_dict, key=lambda fruit: fruits_dict[fruit])
    return (max_entries_name, fruits_dict[max_entries_name])


max_fruits_tuple: tuple[str, int] = get_fruits_entry(fruits)
max_name, max_value = max_fruits_tuple
print(f'{max_name} - {max_value}')

# -----------------------------------------------------------
