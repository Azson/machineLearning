# include <stdio.h>
# include <math.h>

using namespace std;


typedef long long LL;

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 
     * @param n long长整型 表示标准完全二叉树的结点个数
     * @return long长整型
     */
    LL mod = 998244353; 
    LL v = 499122177;
    int get_deps(LL x) {
        int ret = 0;
        x ++;
        while (x) {
            ret ++;
            x >>= 1;
        }
        return ret;
    }
    //(a_1+a_n)*n/2 -> (a_1+a_1+n-1) * n /2
    // (2*a_1 + (n-1)) * n / 2
    long long tree4(long long n) {
        // write code here
        int dep = get_deps(n);
        LL ans = 0, t;
        LL res = 0;
        if (abs(pow(2, dep) - 1 - n) > 0.00001) {
            res = n-pow(2, dep-1)+1;
            dep --;
        }
        for (int i = 1;i <= dep;i++) {
            t = (LL)pow(2, i-1) % mod;
            ans = (ans + (LL)((((3*t-1)*t %mod)*v %mod)*i %mod) %mod) % mod;
        }
        if (res > 0) {
            dep ++;
            t = (LL)pow(2, dep-1) % mod;
            ans = (ans + (LL)(((2*t+res-1) * res %mod) * v %mod) * dep %mod) % mod; 
        }
        return ans;
    }
};

int main()
{
    Solution obj = Solution();
    printf("%lld\n", obj.tree4(5));
}