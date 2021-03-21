
# include <cstdio>
# include <vector>

using namespace std;

int main()
{
	/********** Begin **********/
	int n,m;
    scanf("%d%d", &n, &m);
    vector<vector<int> > a(n, vector<int> (m));
    vector<vector<int> > sm(n+1, vector<int> (m+1));
    for (int i = 0;i < n;i++) {
        for (int j = 0;j < m;j++) {
            scanf("%d", &a[i][j]);
        }
    }
    for (int i = 1;i <= n;i++) {
        for (int j = 1;j <= m;j++) {
            sm[i][j] = sm[i][j-1] + sm[i-1][j] - sm[i-1][j-1] + a[i-1][j-1];
           // printf("%d ", sm[i][j]);
        }
       // printf("\n");
    }

    int ans = INT_MIN;
    for (int i = 1;i <= n;i++) {
        for (int j = 1;j <= m;j++) {
            for (int k = i;k <= n;k++) {
                for (int l = j;l <= m;l++) {
                    ans = max(ans, sm[k][l] - sm[k][j-1] - sm[i-1][l] + sm[i-1][j-1]);
                    //printf("(%d, %d) -> (%d, %d) = %d\n", i, j, k, l, sm[k][l] - sm[k][j-1] - sm[i-1][l] + sm[i-1][j-1]);
                }
            }
        }
    }
    printf("%d\n", ans);
    /**********  End  **********/
	return 0;
}