N = int(input())
test = [input() for i in range(N)]
for i in range(N):
    result = 0
    count = 0
    for j in range(len(test[i])):
        if test[i][j] == 'O':
            count += 1
            result += count
        else:
            count = 0
    print(result)