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
int a[510][510];
int ans;


int fa[1010];

struct node {
    int x, y, v;
    node(int _x, int _y, int _v) {
        x = _x;
        y = _y;
        v = _v;
    }
    node() {}
    bool operator < (const node& t) const {
        return v < t.v;
    }
}now;

int find_fa(int x) {
    return fa[x] == x?x:fa[x] = find_fa(fa[x]);
}

int main() {

    int T, t;
    scanf("%d", &T);
    for (int cas = 1;cas <= T;cas ++) {
        ans = 0;
        scanf("%d", &n);
        for (int i = 0;i < n;i++) {
            for (int j = 0;j < n;j++) {
                scanf("%d", &a[i][j]);
            }
        }
        priority_queue<node> pqe;
        for (int i = 0;i < n;i++) {
            for (int j = 0;j < n;j++) {
                scanf("%d", &t);
                if (a[i][j] == -1) {
                    ans += t;
                    pqe.push(node(i, j+n, t));
                }
            }
        }
        for (int i = 0;i < 2*n;i++) {
            scanf("%*d");
            fa[i] = i;
        }
        while (!pqe.empty()) {
            now = pqe.top();
            pqe.pop();
            if (find_fa(now.x) != find_fa(now.y)) {
                // printf("del %d - %d v %d\n", now.x, now.y, now.v);
                fa[fa[now.x]] = fa[now.y];
                ans -= now.v;
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