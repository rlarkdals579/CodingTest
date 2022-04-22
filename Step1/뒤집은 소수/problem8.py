import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
nums = list(map(int,input().split()))


def reverse(x):
    res = 0
    while x >0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for x in nums:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end = " ")