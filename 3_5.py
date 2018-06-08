# 3번 반복 - i가 0, 1, 2인 동안 반복
for i in range(3):
    print(i)

# i를 5, 6, 7인 동안 반복
for i in range(5, 8):
    print(i)
# i의 증감 폭 지정
for i in range(0, 6, 2):
    print(i)

for i in range(5, 0, -2):
    print(i)
    
# x가 리스트의 원소
a = [10, 20, 30]
for x in a:
    print(x)

# for를 사용한 메뉴 출력
menu = ['','Americano', 'Latte', 'Espresso', 'Mocha', '식혜', '수정과']
price = [0,1500, 2000, 1700, 2500, 2000, 1900]

#메뉴 보이기
for i in range(1,7) :
    print(i, menu[i], price[i])
