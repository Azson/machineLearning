# include <cstdio>
# include <string>
# include <vector>

using namespace  std;

class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 
     * @param n int整型 
     * @param u int整型vector 
     * @param v int整型vector 
     * @return int整型
     */
    vector<int> G[5010];
    bool vis[5010];
    int dep[5010], ans = -1;
    void dfs(int u, int p) {
        vis[u] = true;
        dep[u] = 0;
        for (int i = 0, v;i < G[u].size();i++) {
            v = G[u][i];
            if (!vis[v] && p != v) {
                dfs(v, u);
                // for multi son
                if (ans < dep[u] + dep[v] + 1) {
                    ans = dep[u] + dep[v] + 1;
                }
                if (dep[u] < dep[v] + 1) {
                    dep[u] = dep[v] + 1;
                }
            }
        }
    }
    int MaxDiameter(int n, vector<int>& u, vector<int>& v) {
        // write code here
        ans = -1;
        for (int i = 0;i < n;i++) {
            for (int j = 0;j < n;j++) {
                G[j+1].clear();
                vis[j+1] = false;
            }
            for (int j = 0;j < n;j++) if (i != j) {
                G[u[j]].push_back(v[j]);
                G[v[j]].push_back(u[j]);
            }
            dfs(1, 0);
        }
        return ans;
    }
};