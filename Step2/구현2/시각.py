import sys

sys.stdin = open("input.txt", "rt")

n = int(input())  # n = 5니까 5시 59분 59초까지 3이 포함되는 모든 경우의 수

cnt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 3이 포함되어 있으면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)

