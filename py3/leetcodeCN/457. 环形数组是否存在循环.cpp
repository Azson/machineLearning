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

class Solution {
public:
    int n;

    bool circularArrayLoop(vector<int>& nums) {
        // vector<vector<int> > pos (5005, vector<int> (3));
        
        n  = nums.size();
        auto next = [&](int u) {
            return ((u + nums[u]) % n + n) % n;
        };
        for (int i = 0;i < n;i++) {
            if (!nums[i]) {
                continue;
            }
            int slow = i, fast = next(i);
            while (nums[slow] * nums[fast] > 0 && nums[slow] * nums[next(fast)] > 0) {
                if (slow == fast) {
                    if (slow != next(slow)) {
                        return true;
                    }
                    break;
                }
                slow = next(slow);
                fast = next(next(fast));
            }
            slow = i;
            while (nums[slow] * nums[next(slow)] > 0) {
                fast = slow;
                slow = next(slow);
                nums[fast] = 0;
            }
        }
        return false;
    }
};


int main()
{
    return 0;
}