# include <cstdio>
# include <stack>
# include <vector>
# include <algorithm>
# include <queue>
# include <cstring>

using namespace std;


class Solution {
public:
    int n;

    bool canJump(vector<int>& nums) {
        n = nums.size();
        int right = 0;
        for (int i = 0;i < n;i++) {
            if (i <= right) {
                right = max(right, i+nums[i]);
                if (right >= n-1) {
                    return true;
                }
            }
        }
        return false;;
    }
};

class Solution {
public:
    int n;
    bool vis[30050];
    bool ok(int now, vector<int>& nums) {
        // printf("vis %d\n", now);
        if (vis[now] == false) {
            return false;
        }
        if (now + nums[now] >= n-1) {
            printf("find!\n");
            return true;
        }
        
        for (int i = 1; i <= nums[now] && now+i < n;i++) {
            if (ok(now+i, nums)) {
                return true;
            }
        }
        vis[now] = false;
        return false;
    }

    bool canJump(vector<int>& nums) {
        n = nums.size();
        memset(vis, true, sizeof(vis));
        return ok(0, nums);
    }
};


int main() {

    return 0;
}