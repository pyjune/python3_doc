# 리스트
h = [170,168,173,174]
print(h)
print(h[0])
print(h[1])
print(h[2])
print(h[3])
print(h[-1])    # 맨 마지막 원소
print(h[-2])    # 끝에서 두번째 원소

# 비어있는 리스트 만들기와 원소 추가하기
h1 = []
h2 = list()
h.append(165)
h1.append(150)
h2.append(170)
print(h, h1, h2)

# 원소 제거
h.pop(2)            # 인덱스 사용
print(h)
h.remove(168)       # 값 사용
print(h)

# 리스트의 일부만 표시
print(h[1:3])  #h[1]부터 h[3] 앞까지 출력
print(h[1:])   #h[1]부터 리스트 끝까지 출력
print(h[:3])   #리스트 맨 앞부터 h[3] 앞까지 출력

