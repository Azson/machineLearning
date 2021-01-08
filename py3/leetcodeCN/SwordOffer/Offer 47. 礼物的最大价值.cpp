class Solution {
public:
    int maxValue(vector<vector<int>>& grid) {
        int m = grid.size(), n;
        if (m > 0) n = grid[0].size();
        vector<vector<int> > dp(210, vector<int> (210));
        for (int i = 0;i < m;i++) {
            for (int j = 0;j < n;j++) {
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1]) + grid[i][j];
            }
        }
        return dp[m][n];
    }
};