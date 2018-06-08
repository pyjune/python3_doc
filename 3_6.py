menu = ['','Americano', 'Latte', 'Espresso', 'Mocha', '식혜', '수정과', 'Lemonade']
price = [0,1500, 2000, 1700, 2500, 2000, 1900, 2200]

# for로 출력하는 경우
for i in range(1,len(menu)) :
    print(i, menu[i], price[i])

# while로 출력하는 경우
i = 1
while i< len(menu):
    print(i, menu[i], price[i])
    #print("%d. %-10s %5d"% (i, menu[i], price[i]))
    i = i+1
