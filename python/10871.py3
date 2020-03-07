x = int(input().split()[1])
value = [i for i in map(int,input().split()) if i<x]
print(' '.join(map(str,value)))