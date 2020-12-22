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
     * @param k int整型 
     * @param Point int整型vector 
     * @return int整型vector
     */
    typedef long long LL;
    const LL mod = 1000000007;
    LL fact[200110], inv[200110];
    LL qsm(LL a, LL b) {
        LL ret = 1;
        while (b > 0) {
            if (b&1)
                ret = (ret*a) %mod;
            a = (a*a) %mod;
            b >>= 1;
        }
        return ret;
    }
    void init(int n)
    {
        fact[0] = 1;
        for (int i = 1; i <= n+10; i++)
            fact[i] = fact[i - 1] * i % mod;
        for (int i = 0; i <= n+10; i++)
            inv[i] = qsm(fact[i], mod - 2);
    }
    
    long long C(int n, int m)
    {
        if (m > n) return 0;
        return fact[n] * inv[n - m] % mod * inv[m] % mod;
    }
    vector<int> city(int n, int k, vector<int>& Point) {
        // write code here
        init(n);
        LL fm = qsm(C(n, k), mod-2);
        vector<int> ans(n, 0);
        
        
        vector<pair<int, int> > tmp;
        for (int i = 0;i < n;i++) {
            tmp.push_back(make_pair(Point[i], i));
        }
        sort(tmp.begin(), tmp.end());
        for (int i = 0;i < n;i++) {
            ans[tmp[i].second ] = (C(i, k-1)*fm %mod + mod) %mod;
            //printf("%d -> %d\n", tmp[i].second, ans[tmp[i].second]);
        }
        return ans;
    }
};

int main(int argc, char const *argv[])
{
    //4,[0,1,2],[1,2,3],[1,2,2,1]
    Solution obj = Solution();
    int n = 4;
    vector<int> v;
    //u.push_back(0); u.push_back(1); u.push_back(2);
    v.push_back(1); v.push_back(2); v.push_back(3);
    //p.push_back(1); p.push_back(2); p.push_back(2); p.push_back(1);
    //printf("%lld\n", obj.solve(n, u, v, p));
    obj.city(3, 2, v);
    return 0;
}
