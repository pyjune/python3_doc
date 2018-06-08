# 클래스
class MenuClass:
    menu = ['','Americano', 'Latte', 'Espresso', 'Mocha', '식혜', '수정과']
    price = [0,1500, 2000, 1700, 2500, 2000, 1900]
    bill = [0, 10000, 5000, 1000]
    #############################
    # 메뉴 보이기
    def menu_print(self):
        i = 1
        while i< len(self.menu):
            print(i, self.menu[i], self.price[i])
            i = i+1
            
menu1 = MenuClass()

menu1.menu_print()
