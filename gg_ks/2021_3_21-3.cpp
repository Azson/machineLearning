# include <cstdio>
# include <vector>
# include <string>
# include <cstring>
# include <algorithm>
# include <stack>
# include <queue>
# include <set>

using namespace std;

typedef long long LL;

using namespace std;


int mat[310][310];
int m, n;
LL ans;
int dy[] = {-1, 0, 1, 0};
int dx[] = {0, 1, 0, -1};


struct node {
    int v, y, x;
    node() {}
    node(int _y, int _x, int _v) {
        y = _y;
        x = _x;
        v = _v;
    }
    bool operator < (const node& t) const {
        return v < t.v;
    }
};

int main() {

    int T;
    scanf("%d", &T);
    for (int cas = 1;cas <= T;cas++) {
        scanf("%d%d", &m, &n);
        priority_queue<node> pqe;
        node now;
        ans = 0;
        for (int i = 0;i < m;i++) {
            for (int j = 0;j < n;j++) {
                scanf("%d", &mat[i][j]);
                if (mat[i][j])
                    pqe.push(node(i, j, mat[i][j]));
            }
        }
        int n_y, n_x;
        while (true) {
            while (!pqe.empty() && mat[pqe.top().y][pqe.top().x] != pqe.top().v) pqe.pop();
            if (pqe.empty()) {
                break;
            }
            now = pqe.top();
            pqe.pop();

            for (int dir = 0;dir < 4;dir++) {
                n_y = now.y + dy[dir];
                n_x = now.x + dx[dir];
                if (n_y < 0 || n_y >= m || n_x < 0 || n_x >= n || mat[n_y][n_x] >= mat[now.y][now.x]-1) {
                    continue;
                }   
                ans += mat[now.y][now.x] - mat[n_y][n_x] - 1;
                mat[n_y][n_x] = mat[now.y][now.x] - 1;
                pqe.push(node(n_y, n_x, mat[n_y][n_x]));
            }
        }
        // print();
        printf("Case #%d: %lld\n", cas, ans);
    }
    return 0;
}
/*
4
1 3
3 4 3
1 3
3 0 0
3 3
0 0 0
0 2 0
0 0 0
5 5
0 0 0 0 5
0 0 0 0 0
5 0 0 0 0
0 0 0 0 0
0 0 0 0 0 
*/