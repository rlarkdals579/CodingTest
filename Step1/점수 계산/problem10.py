import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
score_lst = list(map(int,input().split()))

sum = 0
cnt = 0

for i in score_lst:
    if i == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)