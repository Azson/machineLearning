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
     * @param m int整型 
     * @param a int整型vector 
     * @param b int整型vector<vector<>> 
     * @return long长整型
     */
    typedef long long LL;
    LL sum[100100];
    long long wwork(int n, int m, vector<int>& a, vector<vector<int> >& b) {
        // write code here
        LL ans = 0;
        for (int i = 0;i < n;i++) 
            sum[i] = a[i];
        for (int i = 0, z, x, c;i < m;i++) {
            z = b[i][0]-1;
            x = b[i][1]-1;
            c = b[i][2];
            sum[z] += c;
            sum[x] += c;
            ans -= c;
        }
        for (int i = 0;i < n;i++) {
            ans += max(sum[i], (LL)0);
        }
        return ans;
    }
};


int main(int argc, char const *argv[])
{
    //4,[0,1,2],[1,2,3],[1,2,2,1]
    return 0;
}
