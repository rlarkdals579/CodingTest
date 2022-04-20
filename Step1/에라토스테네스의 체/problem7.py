import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
primes = []
cnt = 0


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for i in range(n + 1):
    if isPrime(i):
        cnt += 1

print(cnt)