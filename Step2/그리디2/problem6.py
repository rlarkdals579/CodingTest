import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
men = []

for i in range(n):
    height, weight = map(int, input().split())
    men.append((height, weight))
    men.sort(key=lambda x: (x[0], x[1]), reverse=True)

max = 0
cnt = 0

for height, weight in men:
    if weight > max:
        max = weight
        cnt += 1

print(cnt)
