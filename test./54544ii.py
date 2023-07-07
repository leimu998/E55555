import numpy as np

def fcm(data, num_clusters, m, max_iter=100, error=1e-5):
    num_samples = data.shape[0]
    num_features = data.shape[1]
    
    # 初始化隶属度矩阵 U，随机初始化
    U = np.random.rand(num_samples, num_clusters)
    U = np.divide(U, np.sum(U, axis=1)[:, np.newaxis])
    
    # 迭代更新
    for _ in range(max_iter):
        # 计算聚类中心
        centroids = np.divide(np.dot(U.T, data), np.sum(U.T, axis=1)[:, np.newaxis])
        
        # 计算隶属度矩阵
        prev_U = U.copy()
        dist = np.zeros((num_samples, num_clusters))
        for i in range(num_samples):
            for j in range(num_clusters):
                dist[i, j] = np.linalg.norm(data[i] - centroids[j])
        
        U = np.power(dist, -2 / (m - 1))
        U = np.divide(U, np.sum(U, axis=1)[:, np.newaxis])
        
        # 判断终止条件
        if np.linalg.norm(U - prev_U) < error:
            break
    
    return centroids, U

# 示例用法
data = np.array([[1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0],
                 [7.0, 8.0, 9.0],
                 [10.0, 11.0, 12.0]])

num_clusters = 3
m = 2

centroids, U = fcm(data, num_clusters, m)
print("聚类中心：")
print(centroids)
print("隶属度矩阵：")
print(U)
