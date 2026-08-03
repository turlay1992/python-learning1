# Напиши невелику функцію з Literal — наприклад, 
# def change_order_status(order_id: int, status: Literal["pending", "shipped", "delivered"]) -> None
# яка просто друкує повідомлення про зміну статусу.

from typing import Literal, TypeAlias

OrderStatus: TypeAlias = Literal['pending', 'approved', 'rejected']
class Order:
    def __init__(self, order_id: int, status: OrderStatus = 'pending') -> None:
        self.id: int = order_id
        self.status: OrderStatus = status
        
        
def create_order(order_id: int, status: OrderStatus = 'pending') -> Order:
    return Order(order_id, status)

def change_order_status(order_id: int, status: OrderStatus) -> None:
    old_status: OrderStatus = orders[order_id].status
    orders[order_id].status = status
    print(f'Status of item with {order_id=} was changed from {old_status} to {status}')


orders: dict[int, Order] = {}
for i in range(1, 6):
    orders[i] = create_order(i)
    
try:
    change_order_status(1, 'approved')
    change_order_status(3, 'rejected')
    change_order_status(6, 'approved')
except KeyError as e:
    print(f'Error: {e}')
