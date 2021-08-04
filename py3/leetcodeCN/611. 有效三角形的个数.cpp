# include <cstdio>
# include <vector>
# include <algorithm>


using namespace std;


// class Solution {
// public:
//     int triangleNumber(vector<int>& nums) {
//         int n = nums.size(), ans = 0;
//         sort(nums.begin(), nums.end());
//         for (int i = 0;i < n;i++) {
//             for (int j = i+2;j < n;j++) {
//                 int k = upper_bound(nums.begin(), nums.end(), nums[j]-nums[i]) - nums.begin();
//                 if (k <= i) {
//                     ans += j-i-1;
//                 }
//                 else if (k < j) {
//                     ans += j-k;
//                 }
                
//             }
//         }
//         return ans;
//     }
// };


int bina_search(vector<int>& nums, int l, int r, int x) {
    int m, ret = 1000000;
    while (l <= r) {
        m = (l + r) / 2;
        printf("%d, %d -> %d\n", l, r, m);
        if (nums[m] <= x) {
            l = m+1;
        }
        else {
            ret = m;
            r = m-1;
        }
    }
    return ret;
}

class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        sort(nums.begin(), nums.end());
        for (int i = 0;i < n;i++) {
            for (int j = i+2;j < n;j++) {
                int k = bina_search(nums, i+1, j-1, nums[j]-nums[i]);
                if (k <= i) {
                    ans += j-i-1;
                }
                else if (k < j) {
                    ans += j-k;
                }
                
            }
        }
        return ans;
    }
};

int main() {

    vector<int> vec = {1,1,3,4};
    Solution so = Solution();
    printf("%d\n", so.triangleNumber(vec));
}