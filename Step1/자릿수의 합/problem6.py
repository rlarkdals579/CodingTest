import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
nums = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


def digit_sum2(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


max = -2147000000
for x in nums:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x

print(res)
