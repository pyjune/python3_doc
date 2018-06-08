menu = ['','Americano', 'Latte', 'Espresso', 'Mocha', '식혜', '수정과']
price = [0,1500, 2000, 1700, 2500, 2000, 1900]
bill = [0, 10000, 5000, 1000]

#############################
# 메뉴 보이기
def menu_print():
    i = 1
    while i< len(menu):
        print(i, menu[i], price[i])
        #print("%d. %-10s %5d"% (i, menu[i], price[i]))
        i = i+1
#############################

menu_print()
# 음료  선택
n = int(input("음료를 선택하세요 : "))
total = price[n] 
print(menu[n], price[n],'원 ', '합계 ', total, '원')
