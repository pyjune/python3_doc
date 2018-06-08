# 기본 형식
for i in range(1, 10):      # 줄 번호 1~9
    for j in range(1, i+1): # 별의 개수 1~9
        print('*', end='')
    print()                 # 한 줄이 끝나면 새줄로 바꿈
    
# 파이썬의 형식 사용
for j in range(1, 10):
    print('*' * j)   # '*'를 j번 출력
