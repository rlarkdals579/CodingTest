import sys
from collections import Counter

sys.stdin = open("input.txt", "rt")

N, M = map(int,input().split())

nList = []
mList = []
sumList = []
cnt = 0

for x in range(N):
    nList.append(x+1)

for x in range(M):
    mList.append(x+1)

for x in nList:
    for y in mList:
        sumList.append(x + y)

counter = Counter(sumList)
all_values = counter.values()
max_value = max(all_values)

for key in counter:
    if counter[key] == max_value:
        print(key,end=" ")


