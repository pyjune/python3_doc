# 0번부터 사용하는 경우
menu = ['Americano', 'Latte', 'Espresso', 'Mocha', '식혜', '수정과']
price = [1500, 2000, 1700, 2500, 2000, 1900]
n = int(input("음료를 선택하세요 : "))

print(menu[n], price[n],'원')

# 1번부터 사용하는 경우
menu = ['','Americano', 'Latte', 'Espresso', 'Mocha', '식혜', '수정과']
price = [0,1500, 2000, 1700, 2500, 2000, 1900]
n = int(input("음료를 선택하세요 : "))

print(menu[n], price[n],'원')

# 전체 메뉴 보이기
menu = ['','Americano', 'Latte', 'Espresso', 'Mocha', '식혜', '수정과']
price = [0,1500, 2000, 1700, 2500, 2000, 1900]

#메뉴 보이기
i = 1
while i <= 6:
    print(i, menu[i], price[i])
    i = i+1

#메뉴 선택
n = int(input("음료를 선택하세요 : "))
print(menu[n], price[n],'원')
