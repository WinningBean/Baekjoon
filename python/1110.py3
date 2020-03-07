N = value = int(input())
c = 0
while value != N or c==0:
    value = value%10*10 + (value//10+value%10)%10
    c+=1
print(c)