import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
k = list(map(int, input().split()))
k.sort()
print(k)

result = 0
count = 0

for i in k:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)



