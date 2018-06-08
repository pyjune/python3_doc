# __init__()
class MenuClass:
    def __init__(self):
       self.menu = ['','Americano', 'Latte', 'Espresso', 'Mocha', '식혜', '수정과']
       self.price = [0,1500, 2000, 1700, 2500, 2000, 1900]
       self.bill = [0, 10000, 5000, 1000]
       self.total = 0
       
menu1 = MenuClass()
menu2 = MenuClass()

menu1.price[1] = 2500
print(menu1.price[1], menu2.price[1])
