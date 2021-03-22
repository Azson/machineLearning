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

int n;
int a[1010][1010];
int b[1010][1010];
int ans;
bool vis[1010];


struct node {
    int x, v;
    node(int _x, int _v) {
        x = _x;
        // y = _y;
        v = _v;
    }
    node() {}
    bool operator < (const node& t) const {
        return v < t.v;
    }
}now;


int main() {

    int T;
    // freopen("/Users/azson/Desktop/gg_2021_r_a/test_data/test_set_1/ts1_input.txt", "r", stdin);
    scanf("%d", &T);
    for (int cas = 1;cas <= T;cas ++) {
        ans = 0;
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        scanf("%d", &n);
        for (int i = 0;i < n;i++) {
            for (int j = 0;j < n;j++) {
                scanf("%d", &a[i][j+n]);
                a[j+n][i] = a[i][j+n];
            }
        }
        priority_queue<node> pqe;
        for (int i = 0;i < n;i++) {
            for (int j = 0;j < n;j++) {
                scanf("%d", &b[i][j+n]);
                b[j+n][i] = b[i][j+n];
                if (a[i][j+n] == -1) {
                    ans += b[i][j+n];
                    pqe.push(node(i, 0));
                }
            }
        }
        for (int i = 0;i < 2*n;i++)  {
            scanf("%*d");
        }

        memset(vis, false, sizeof(vis));
        // pqe.push(node(0, 0));
        while (!pqe.empty()) {
            now = pqe.top();
            pqe.pop();
            if (vis[now.x]) {
                continue;
            }
            // printf("vis %d v %d size %d ans %d\n", now.x, now.v, (int)pqe.size(), ans);
            vis[now.x] = true;
            ans -= now.v;
            for (int j = 0;j < 2*n;j++) if (!vis[j] && a[now.x][j] == -1) {
                // printf("in (%d -> %d) %d\n", now.x, j, b[now.x][j]);
                pqe.push(node(j, b[now.x][j]));
            }
        }


        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}

/*
3
3
1 -1 0
0 1 0
1 1 1
0 1 0
0 0 0
0 0 0
1 1 1
0 0 1
2
-1 -1
-1 -1
1 10
100 1000
1 0
0 1
3
-1 -1 -1
-1 -1 -1
0 0 0
1 1 3
5 1 4
0 0 0
0 0 0
0 0 0

*/