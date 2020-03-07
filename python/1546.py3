print("")
N = int(input())
value = list(map(int,input().split()))
sum = 0
M = max(value)
for i in range(N):
    value[i] = value[i]/M*100
    sum += value[i]
print('%.2f'%(sum/N))
