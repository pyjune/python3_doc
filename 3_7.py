# if를 사용한 입력 확인
menu = ['','Americano', 'Latte', 'Espresso', 'Mocha', '식혜', '수정과', 'Lemonade']
price = [0,1500, 2000, 1700, 2500, 2000, 1900, 2200]

n = int(input("음료를 선택하세요 : "))
if (n>=1 and n<=7) :
    print(menu[n], price[n],'원')
else :
    print("잘못된 입력입니다.")

# 숨어있는 메뉴
n = int(input("음료를 선택하세요 : "))
if (n>=1 and n<=7) :
    print(menu[n], price[n],'원')
else :
    if n == 99 :
        print("매출 정산을 시작합니다.")
    else :
        print("잘못된 입력입니다.")
