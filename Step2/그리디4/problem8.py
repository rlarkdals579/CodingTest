import sys
from _collections import deque

sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = deque(a)


def dequeGreedy():
    cnt = 0

    while a:
        if len(a) == 1:
            cnt += 1
            break

        if a[0] + a[-1] > k:
            a.pop()
            cnt += 1

        else:
            a.popleft()
            a.pop()
            cnt += 1

    return cnt


def listGreedy():
    cnt = 0
    while a:
        if len(a) == 1:
            cnt += 1
            break

        if a[0] + a[-1] > k:
            a.pop()
            cnt += 1

        else:
            a.pop(0)
            a.pop()
            cnt += 1

    return cnt


print(dequeGreedy())
