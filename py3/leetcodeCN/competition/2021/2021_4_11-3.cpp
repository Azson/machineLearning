# include <cstdio>
# include <vector>
# include <algorithm>
# include <iostream>

using namespace std;

class Solution {
public:
    int minSideJumps(vector<int>& obstacles) {
        int n = obstacles.size();
        vector<vector<int> > dp(n+1, vector<int>(3, 9999999));
        dp[0][0] = dp[0][2] = 1;
        dp[0][1] = 0;
        for (int i = 1;i < n;i++) {
            for (int j = 0;j < 3;j++) {
                if (obstacles[i] == j+1) {
                    dp[i][j] = -1;
                    continue;
                }

                for (int k = 0;k <= 2;k++) {
                    if (dp[i-1][(j+k) % 3] >= 0 && obstacles[i] != (j+k) % 3 + 1) {
                        dp[i][j] = min(dp[i][j], dp[i-1][(j+k) % 3]+(k == 0?0:1));
                    }
                }
            }
        }

        int ans = 9999999;
        for (int i = 0;i < 3;i++) {
            if (dp[n-1][i] != -1) {
                ans = min(ans, dp[n-1][i]);
            }
        }
        return ans;
    }
};
int main() {
    Solution sol = Solution();
    vector<int> vec {0,2,1,0,3,0};
    printf("%d\n", sol.minSideJumps(vec));
}