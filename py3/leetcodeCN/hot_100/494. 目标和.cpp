# include <cstdio>
# include <stack>
# include <vector>
# include <algorithm>
# include <queue>
# include <cstring>
# include <map>

using namespace std;


class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        int sm = 0, neg;
        int ans = 0;
        for (int& x : nums) {
            sm += x;
        }

        if (sm < target || (sm - target) % 2) {
            return 0;
        }
        neg = (sm - target) / 2;
        vector<int> dp(neg);
        for (int& x : nums) {
            for (int i = neg;i >= x;i--) {
                dp[i] += dp[i - x];
            }
        }
        return dp[neg];
    }
};


int main() {

    return 0;
}