import sys
sys.stdin = open("input.txt", "rt")

sum = []
new_sum = []
n, k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

for x in range(len(a)-1):
    for y in range(2,len(a)-2):
        sum.append(a[x] + a[x+1] + a[y])
        sum.sort(reverse=True)

for a in sum:
    if a not in new_sum:
        new_sum.append(a)

print(new_sum[k-1])
