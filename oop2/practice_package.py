from cusorder.costomer import Customer
from cusorder.order import Order
cus1 = Customer("Jame","Nonthaburi")
order1 = Order("15-06-2022","Packed")
print(f'order of {cus1.name} no {order1.date} is {order1.status}')
