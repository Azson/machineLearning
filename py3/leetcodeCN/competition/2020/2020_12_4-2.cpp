# include <cstdio>
# include <string>
# include <vector>
# include <cmath>
# include <algorithm>
# include <queue>

using namespace std;

class Solution {
public:
    /**
     * 
     * @param n int整型 乐谱总音符数
     * @param m int整型 重音符数
     * @param k int整型 重音符之间至少的间隔
     * @return long长整型
     */
    /*
    need t1 = (m-1)*(k+1)+1
    for k in (k, n):
        ans += n % t1
    */
    typedef long long LL;
    const LL mod = 1000000007;
    long long solve_bangbang(int n, int m, int k) {
        // write code here
        vector<vector<int> > dp (n+1, vector<int> (m+1, 0));
        dp[0][0] = 1;
        for (int i = 1;i <= n;i++) {
            dp[i][0] = dp[i-1][0];
            for (int j = 1;j <= m && j <= i;j++) {
                dp[i][j] = dp[i-1][j];
                dp[i][j] += dp[max(i-k-1, 0)][j-1];
                if (dp[i][j] >= mod) dp[i][j] %= mod;
            }
        }
        return dp[n][m];
    }
};


int main(int argc, char const *argv[])
{
    Solution obj = Solution();
    printf("%lld\n", obj.solve_bangbang(3, 2, 1));
    return 0;
}
