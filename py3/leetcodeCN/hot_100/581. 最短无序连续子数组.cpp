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

    int findUnsortedSubarray(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        int left = -1, right = -1, mn = INT_MAX, mx = INT_MIN;
        for (int i = 0;i < n;i++) {
            if (mn < nums[n - i - 1]) {
                left = n - i - 1;
            } else {
                mn = nums[n - i - 1];
            }

            if (mx > nums[i]) {
                right = i;
            } else {
                mx = nums[i];
            }
        }
        // printf("left %d, %d\n", left, right);
        return left < right ? right - left + 1 : 0;
    }
};


int main() {

    return 0;
}