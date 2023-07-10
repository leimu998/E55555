from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(input())

st = [[False for i in range(m)] for j in range(n)]

block = [[],[]]
# def dfs(block,x,y):
#     st[x][y] = True
#     block.append((x,y))
#     for i in range(4):
#         nx,ny = x+dx[i],y+dy[i]
#         if nx < 0 or ny < 0 or nx >=n or ny >= m: continue
#         if st[nx][ny] or g[nx][ny] != 'X':continue
#         dfs(block,nx,ny)

q = deque()
def bfs(block,x,y):
    q.append((x,y))
    st[x][y] = True

    while q:
        t = q.popleft()
        block.append(t)#记录坐标

        for i in range(4):
            nx,ny = t[0]+dx[i],t[1]+dy[i]
            if nx >=0 and nx < n and ny >=0 and ny < m and g[nx][ny] == 'X' and not st[nx][ny]:
                st[nx][ny] = True
                q.append((nx,ny))


cnt = 0
for i in range(n):
    for j in range(m):
        if not st[i][j] and g[i][j] == 'X': 
            bfs(block[cnt],i,j)
            cnt += 1

res = 10**9
for x1 in block[0]:
    for x2 in block[1]:
        res = min(res,abs(x1[0]-x2[0]) + abs(x1[1]-x2[1])-1)

print(res)

作者：AcWing
链接：https://www.acwing.com/activity/content/189/
来源：AcWing
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
