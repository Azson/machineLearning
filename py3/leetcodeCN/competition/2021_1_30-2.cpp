#pragma warning(disable:4996)

# include <cstdio>
# include <vector>

using namespace std;

int dx[] = {0, 0, -1, 1, -1, -1, 1, 1};
int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};

void solve(vector<vector<int> > & a, int last, int now) {
    int sz = a.size();
    for (int i = 1;i < sz;i++) {
        for (int j = 1, k;j < sz;j++) if (a[i][j] == 0) {
            k = 0;
            for (;k < 8;k++) if (i+dy[k] < sz && j+dx[k] < sz){
                if (a[i+dy[k] ][j+dx[k] ] == last) {
                    break;
                }
            }
            if (k != 8) {
                a[i][j] = now;
            }
        }
    }
}

int main()
{
	/********** Begin **********/
	int N, n;
    scanf("%d", &N);
    // 1,4 -> ' ', 2 -> '$', 3 -> '.'
    vector<vector<int> > a(4*N+5+1, vector<int> (4*N+5+1));
    n = 4*N+5;
    int mid = 4;
    if (N % 2 == 0) {
        
        mid = 2;
    }
    a[(n+1)/2][(n+1)/2] = mid;
    for (int i = 0;i < 4;i++) {
        for (int j = 1;j <= 2;j++) {
            //printf("(%d, %d)\n", (n+1)/2 + dy[i]*j, (n+1)/2 + dx[i]*j);
            a[(n+1)/2 + dy[i]*j ][(n+1)/2 + dx[i]*j ] = mid;
        }
    } 
    if (N % 2) {
        a[1][1] = 5;
        a[1][n] = a[n][1] = a[n][n] = 5;
    }
    int last = 3;
    solve(a, mid, last);
    mid = 2;
    for (int i = 0;i < N*2;i++) {
        solve(a, last, mid);
        swap(last, mid);
    }

    if (N % 2 == 0) {
        int y,x;
        x = y = 1;
        a[y][x] = 1;
        for (int i = 0;i < 8;i++) if (x + dx[i] <= n && y + dy[i] <= n && x + dx[i] >= 0 && y + dy[i] >= 0 ) {
            a[y+dy[i]][x+dx[i]] = 1;
        }

        x = n, y = 1;
        a[y][x] = 1;
        for (int i = 0;i < 8;i++) if (x + dx[i] <= n && y + dy[i] <= n && x + dx[i] >= 0 && y + dy[i] >= 0 ) {
            a[y+dy[i]][x+dx[i]] = 1;
        }
        x = 1, y = n;
        a[y][x] = 1;
        for (int i = 0;i < 8;i++) if (x + dx[i] <= n && y + dy[i] <= n && x + dx[i] >= 0 && y + dy[i] >= 0 ) {
           a[y+dy[i]][x+dx[i]] = 1;
        }
        x = n, y = n;
        a[y][x] = 1;
        for (int i = 0;i < 8;i++) if (x + dx[i] <= n && y + dy[i] <= n && x + dx[i] >= 0 && y + dy[i] >= 0 ) {
            a[y+dy[i]][x+dx[i]] = 1;
        }
    }
    if (N % 2) {
        for (int i = 1;i <= n;i++) {
            a[(n+1)/2][i] = 4;
            a[i][(n+1)/2] = 4;
        }
        
    }
    for (int i = 1;i <= n;i++) {
        for (int j = 1;j <= n;j++) {
            if (a[i][j] == 1 || a[i][j] == 4) {
                printf(" ");
            }
            else if (a[i][j] == 2) {
                printf("$");
            }
            else if (a[i][j] == 3 || a[i][j] == 5) {
                printf(".");
            }
        }
        printf("\n");
    }
    /**********  End  **********/
	return 0;
}