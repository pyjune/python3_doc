a = [7, 2, 1, 8, 9, 10]

# max() 메소드 사용
#print(max(a))

maxValue = a[0]
for i in range(1, len(a)):
    if maxValue < a[i]:
        maxValue = a[i]
print(maxValue)
