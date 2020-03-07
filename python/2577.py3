A = int(input())
B = int(input())
C = int(input())
mysum = list(map(int,list(str(A*B*C))))
[print(mysum.count(i)) for i in range(10)]