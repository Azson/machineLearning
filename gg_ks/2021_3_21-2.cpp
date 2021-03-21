# include <cstdio>
# include <vector>
# include <cstring>
# include <algorithm>

using namespace std;

typedef long long LL;

using namespace std;

int n, m;
int grid[1010][1010];
int dx[] = {0, 1, 0, -1};
int dy[] = {-1, 0, 1, 0};
int pre_sum[1010][1010][4];
LL ans;


int main() {

    int T;
    scanf("%d", &T);
    for (int cas = 1;cas <= T;cas++) {
        scanf("%d%d", &m, &n);
        ans = 0;
        memset(pre_sum, 0, sizeof(pre_sum));
        for (int i = 0;i < m;i++) {
            for (int j = 0;j < n;j++) {
                scanf("%d", &grid[i][j]);
            }
        }
        for (int i = 0;i < m;i++) {
            for (int j = 0;j < n;j++) if (grid[i][j]) {
                pre_sum[i+1][j+1][1] = pre_sum[i+1][j][1] + 1;
                pre_sum[i+1][j+1][2] = pre_sum[i][j+1][2] + 1;
            } 
        }
        for (int i = m-1;i >= 0;i--) {
            for (int j = n-1;j >= 0;j--) if (grid[i][j]) {
                pre_sum[i+1][j+1][0] = pre_sum[i+2][j+1][0] + 1;
                pre_sum[i+1][j+1][3] = pre_sum[i+1][j+2][3] + 1;
            }
        }

        for (int i = 1;i <= m;i++) {
            for (int j = 1;j <= n;j++) if (grid[i-1][j-1]) {
                for (int dir = 0;dir < 4;dir ++) {
                    ans += max(0, min(pre_sum[i][j][dir], pre_sum[i][j][(dir+1)%4] /2) -1);
                    ans += max(0, min(pre_sum[i][j][dir], pre_sum[i][j][(dir+3)%4] /2) -1);
                }
            }
        }
        printf("Case #%d: %lld\n", cas, ans);
    }
    return 0;
}

/*
4
4 3
1 0 0
1 0 1
1 0 0
1 1 0
6 4
1 0 0 0
1 0 0 1
1 1 1 1
1 0 1 0
1 0 1 0
1 1 1 0
4 6
1 1 1 1 1 1
0 0 1 0 0 1
0 1 1 1 1 1
0 1 1 0 0 0
4 3
0 1 0
0 1 0
1 1 1
0 1 0
*/