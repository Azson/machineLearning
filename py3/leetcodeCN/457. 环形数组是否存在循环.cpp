# include <cstdio>
# include <vector>
# include <algorithm>
# include <queue>
# include <cstring>

using namespace std;


class Solution {
public:
    bool vis[5005];
    int n;
    bool dfs(int u, int start, int dep, vector<int>& nums) {
        
        int v = (u + nums[u] + n*1000) % n;
        if (start == v) {
            return dep > 1?true:false;
        }
        if (nums[u] * nums[v] < 0 || vis[v]) {
            return false;
        }

        vis[u] = true;
        return dfs(v, start, dep+1, nums);

    }
    bool circularArrayLoop(vector<int>& nums) {      
        n  = nums.size();
        for (int i = 0;i < n;i++) {
            memset(vis, false, sizeof(vis));
            if (dfs(i, i, 1, nums)) {
                return true;
            }
        }
        return false;
    }
};


int main()
{
    return 0;
}