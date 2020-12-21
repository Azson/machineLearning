# include <cstdio>
# include <string>
# include <vector>
# include <algorithm>

using namespace  std;


class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 
     * @param n int整型 
     * @param a int整型vector 
     * @return int整型
     */
    int wwork(int n, vector<int>& a) {
        // write code here
        int ans = 0, mn = n;
        for (int i = n-1;i >= 0;i--) {
            if (a[i] > mn) {
                ans ++;
            }
            mn = min(a[i], mn);
        }
        return ans;
    }
};

