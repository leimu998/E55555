#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> PII;

vector<vector<int>> v, dist;
int n, m;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int bfs() {
    deque<PII> q;
    q.push_back(PII{1, 1});
    dist[1][1] = v[1][1];
    while (!q.empty()) {
        auto t = q.front();
        q.pop_front();
        int x = t.first, y = t.second;
        for (int i = 0; i < 4; i++) {
            int xx = x + dx[i];
            int yy = y + dy[i];
            if (xx < 1 || xx > n || yy < 1 || yy > m)   continue;
            int d = v[xx][yy];
            if (dist[xx][yy] > dist[x][y] + d) {
                dist[xx][yy] = dist[x][y] + d;
                // 这里是双端队列bfs
                if (d == 0) {
                    q.push_front({xx, yy});
                } else {
                    q.push_back({xx, yy});
                }
            }
        }
    }
    return dist[n][m];
}

int main() {
    cin >> n >> m;
    v.resize(n + 1, vector<int>(m + 1, 0));
    dist.resize(n + 1, vector<int>(m + 1, 2e9));
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            cin >> v[i][j];
    cout << bfs() << endl;
    return 0;
}
