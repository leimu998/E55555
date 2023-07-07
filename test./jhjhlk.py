from math import inf
n,m,k = map(int,input().split())
N = 510
d = [[inf for i in range(N)] for j in range(N)]
dist = [inf] * N
st = [False] * N

def dijkstra():
    dist[1] = 0
    for i in range(n-1):
        t = -1
        for j in range(1,n+1):
            if not st[j] and dist[j] < dist[t]:
                t = j
        st[t] = True
        for j in range(1,n+1):
            dist[j] = min(dist[j],dist[t] + d[t][j])
        if t == n:
            break
    if dist[n] == inf:
        return -1
    return dist[n]
    
for _ in range(m):
    x,y,z = map(int,input().split())
    d[x][y] = min(d[x][y],z)

print(dijkstra())
