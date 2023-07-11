# 计算杨辉三角 补0法
triangle = [[1]]
n = int(input())
for i in range(1, n):
    swap = triangle[i-1]+[0]
    cul = [1]
    for j in range(len(swap)-1):
        cul.append(swap[j]+swap[j+1])
    triangle.append(cul)
# print(triangle)

x, y = map(int, input().split(','))

#计算结果
value = triangle[x - 1][y - 1]
# col_sum = sum([ row[y-1] for row in triangle ])
col_sum = 0
for i in range(n-y+1):
    col_sum += triangle[i+1][y-1]

#输出结果
print(value,end = ',')
print(col_sum)
