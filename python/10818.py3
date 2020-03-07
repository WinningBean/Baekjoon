N = int(input())
value = list(map(int,input().split()))
min = value[0]
max = value[0]
for i in range(N):
    if min > value[i]:
        min = value[i]
    if max < value[i]:
        max = value[i]
print(min, max)
