import sys
sys.setrecursionlimit(1000000) #加这么一句可以修改 dfs 深度
from collections import defaultdict
#每棵树最大可能形成的高度为其最深子树的高度(根节点高度为0)+其孩子的数量
N = 100010
g = defaultdict(list)

def dfs(u):
    ans = 0
    cnt = len(g[u])
    for i in range(cnt):
        ans = max(ans,dfs(g[u][i]) + cnt)
    return ans

n = int(input())
for i in range(2,n+1):
    x = int(input())
    g[x].append(i)
    
ans = dfs(1)

print(ans)
