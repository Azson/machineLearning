# include <cstdio>
# include <string>
# include <vector>
# include <algorithm>
# include <cmath>

using namespace  std;


class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 
     * @param arr int整型vector 
     * @param a int整型 
     * @param b int整型 
     * @return int整型
     */
    typedef long long LL;
    const LL mod = 1000000007;
    int countTriplets(vector<int>& arr, int a, int b) {
        // write code here
        LL ans = 0;
        int n = arr.size(), l, r;
       for (int i = 1;i < n-1;i++) {
           l = r = 0;
           for (int j = 0;j < i;j++) {
               if (abs(arr[j] - arr[i]) <= a)   l++;
           }
           for (int j = i+1;j < n;j++) {
               if (abs(arr[j] - arr[i]) <= b)   r++;
           }
           ans = (ans + (LL)l*r%mod) %mod;
       }
        return ans;
    }
};

int main(int argc, char const *argv[])
{
    //4,[0,1,2],[1,2,3],[1,2,2,1]
    Solution obj = Solution();
    vector<int> a;
    a.push_back(7); a.push_back(1); a.push_back(8); a.push_back(9); 
    printf("%lld\n", obj.countTriplets(a, 3, 3));
    return 0;
}
