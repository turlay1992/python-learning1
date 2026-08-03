def describe_product(name: str, price: float, / , currency: str = 'UAH', **kwargs: str | int) -> str:
    response: str = f'Information about {name}. It coast {price} {currency}\nAdditional information:\n'
                    
    for key, value in kwargs.items():
        response += f'{key.capitalize()}: {str(value)}\n'

    return response

print(describe_product('Shoes', 125, color='Black', size=41))

# ---------------------------------------------------------------

