# include <cstdio>
# include <cstdio>
# include <vector>
# include <algorithm>
# include <queue>
# include <cstring>

using namespace std;

class Solution {
public:
    vector<vector<int> > ans;
    int n;
    void dfs(int pos, int res, vector<int> now, vector<int>& candidates) {
        // printf("vis %d, res %d %d,\n", pos, res, now.size());
        if (res == 0) {
            ans.push_back(now);

            return ;
        }
        if (pos >= n || candidates[pos] > res) {
            return ;
        }
        dfs(pos+1, res, now, candidates);

        now.push_back(candidates[pos]);
        dfs(pos, res-candidates[pos], now, candidates);

    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        ans.clear();
        sort(candidates.begin(), candidates.end());
        n = candidates.size();

        dfs(0, target, vector<int> (), candidates);
        return ans;
    }
};


int main() {

    vector<int> a {2,3,6,7};
    int target = 7;
    Solution so = Solution();
    so.combinationSum(a, target);
    return 0;
}