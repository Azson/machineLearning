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
     * @param n int整型 点的个数
     * @param u int整型vector 每条边的起点
     * @param v int整型vector 每条边的终点
     * @param p int整型vector 每个点的价值
     * @return long长整型
     */
    typedef long long LL;
    int fa[100010], sz[100010];

    int find_pa(int x) {
        return fa[x] == x?x:fa[x] = find_pa(fa[x]);
    }

    long long solve(int n, vector<int>& u, vector<int>& v, vector<int>& p) {
        // write code here
        LL ans = 0;
        for (int j = 0;j <= 20;j++) {
            for (int i = 0;i < n;i++) {
                fa[i] = i;
                sz[i] = 0;
            }
            for (int i = 0;i < n-1;i++) {
                if ((p[u[i]] >> j & 1) && (p[v[i]] >> j & 1)) {
                    fa[find_pa(v[i])] = find_pa(u[i]);
                }
            }
            for (int i = 0;i < n;i++) sz[find_pa(i)] ++;
            for (int i = 0;i < n;i++) if (fa[i] == i && (p[i] >> j & 1)) {
                ans += (LL) sz[i] * (sz[i] + 1) / 2 * (1 << j);
            }
        }
        return ans;
    }
};

int main(int argc, char const *argv[])
{
    //4,[0,1,2],[1,2,3],[1,2,2,1]
    Solution obj = Solution();
    int n = 4;
    vector<int> u, v, p;
    u.push_back(0); u.push_back(1); u.push_back(2);
    v.push_back(1); v.push_back(2); v.push_back(3);
    p.push_back(1); p.push_back(2); p.push_back(2); p.push_back(1);
    printf("%lld\n", obj.solve(n, u, v, p));
    return 0;
}
