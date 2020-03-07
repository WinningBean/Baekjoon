N = int(input())
value = [list(map(int,input().split())) for i in range(N)]
for i in range(N):
    count = 0
    stu = value[i][0]
    myavg = (sum(value[i]) - stu)/stu
    for j in range(1,stu+1):
        if value[i][j] > myavg:
            count += 1
    print('{0:.3f}%'.format(round(count/stu*100,3)))