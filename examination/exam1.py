class JuiceOrder:
    menu_type = "Juice"
    total = 0
    def __init__(self,customer_name:str,menu:str,num = 1,size = '') -> None:
      self.customer_name = customer_name
      self.menu = menu.upper()
      self.num = num
      self.size = size.upper()
      self.price = 0
    def check_menu(self):
        menu_dictionary = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30,
        }

        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)
    def compute_price(self):
        if self.size == 'L':
            self.price += 1
        else:
            self.price
        
        JuiceOrder.total = self.price * self.num
    def display_detail(self):
        self.check_menu()
        self.compute_price()
        return f'{self.customer_name}, {self.menu} => {JuiceOrder.total}'
        
if __name__ == "__main__":
    order1 = JuiceOrder("WJ","(L*35)")
    order2 = JuiceOrder("OJ","(R*25)")
    order3 = JuiceOrder("PJ","(L*35)")
    
    print(order1.display_detail())
    print(order2.display_detail())
    print(order3.display_detail())