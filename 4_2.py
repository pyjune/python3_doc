# 한 단만 출력
i = 5
for j in range(1, 10):
    print(i*j, end=' ')    # 새 줄에 출력하는 대신 여백을 두고 이어서 출력
    
# 전체 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=' ')
    print()                   # 한 단이 끝나면 새 줄로 바꿉니다.
