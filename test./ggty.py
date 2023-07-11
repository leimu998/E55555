import functools
N = 20010
M = 110
n = int(input())

place = [[0 for i in range(N)] for j in range(M)]

for i in range(1,6):
    for j in range(1,n+1):
        x = int(input())
        place[i][x] = j #记录每个奶牛的位置
        

a = [x for x in range(1,n+1)]


def mycmp(x,y):
    ans = 0
    for i in range(1,6):
        if place[i][x] < place[i][y]: #满足相对顺序的次数
            ans += 1
    if ans >= 3: return 1
    elif ans < 3: return -1
    else: return 0
    

a.sort(key=functools.cmp_to_key(mycmp))

for x in a: print(x)

