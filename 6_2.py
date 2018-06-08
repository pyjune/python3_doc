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

#############################
# 음료  선택
def menu_select():
    n = int(input("음료를 선택하세요 : "))
    price_sum = price[n] 
    print(menu[n], price[n],'원 ', '합계 ', price_sum, '원')

    # 음료 추가

    while n != 0:
        print()
        n = int(input("계속 주문은 음료 번호를, 지불은 0을 누르세요 : "))
        if n > 0 and n < len(menu):
            price_sum = price_sum + price[n]
            print(menu[n], price[n],'원 ', '합계 ', price_sum, '원')
        else :
            if n == 0 :
                print("주문이 완료되었습니다.")
            else :
                print("없는 메뉴입니다.")
    return price_sum
##############################

menu_print()
total = menu_select()
print(total)
