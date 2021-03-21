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
     * @param n int整型 节点个数
     * @param u int整型vector 
     * @param v int整型vector 
     * @return int整型
     */
    const static int N = 1e5+10;
    vector<int> G[N];
    int dis_mx[N], dis_sec[N], dis_up[N], mx_son[N];
    bool vis[N];
    void dfs_down(int u) {
        int v;
        for (int i = 0;i < G[u].size();i++) if (!vis[G[u][i]]) {
            v = G[u][i];
            vis[v] = true;
            dfs_down(v);
            if (dis_mx[v] + 1 > dis_mx[u]) {
                dis_sec[u] = dis_mx[u];
                dis_mx[u] = dis_mx[v] + 1;
                mx_son[u] = v;
            }
            else if (dis_mx[v] + 1 > dis_sec[u]) {
                dis_sec[u] = dis_mx[v] + 1;
            }
            vis[v] = false;
        }
    }
    void dfs_up(int u) {
        int v;
        for (int i = 0;i < G[u].size();i++) if (!vis[G[u][i]]) {
            v = G[u][i];
            if (mx_son[u] == v) {
                dis_up[v] = max(dis_sec[u], dis_up[u])+1;
            }
            else {
                dis_up[v] = max(dis_mx[u], dis_up[u])+1;
            }
            vis[v] = true;
            dfs_up(v);
            vis[v] = false;
        }
    }
    int PointsOnDiameter(int n, vector<int>& u, vector<int>& v) {
        // write code here
        for (int i = 1;i <= n;i++) {
            G[i].clear();
            mx_son[i] = 0;
            dis_mx[i] = dis_sec[i] = dis_up[i] = 0;
        }
        for (int i = 0;i < u.size();i++) {
            G[u[i]].push_back(v[i]);
            G[v[i]].push_back(u[i]);
        }
        memset(vis, false, sizeof(N));
        vis[1] = true;
        dfs_down(1);
        dfs_up(1);
        vis[1] = false;
        int mx=0, ans=0;
        for (int i = 1;i <= n;i++) {
            //printf("i %d -> mx %d, sec %d, up %d\n", i, dis_mx[i], dis_sec[i], dis_up[i]);
            mx = max(mx, dis_mx[i]+dis_up[i]);
        }
        for (int i = 1;i <= n;i++) {
            if (dis_mx[i]+dis_sec[i]+dis_up[i] - min(dis_sec[i], dis_up[i]) == mx) {
                ans ++;
            }
        }
        return ans;
    }
};


int main(int argc, char const *argv[])
{
    Solution obj = Solution();
    vector<int> u, v;
    u.push_back(1); u.push_back(1); u.push_back(1);
    v.push_back(2); v.push_back(3); v.push_back(4);
    int n = 4;
    printf("%d\n", obj.PointsOnDiameter(n, u, v));
    return 0;
}

/*
class Solution {
public:
    vector<pair<int,int> > vec[100005];
    int dp[100005][3],myson[100005];
    bool vis[100005];
    void dfs1(int root)
    {
        for(int i=0;i<(int)vec[root].size();++i)
        {
            int son = vec[root][i].first;
            int len = vec[root][i].second;
            if(!vis[son])
            {
                vis[son]=true;
                dfs1(son);
                if(dp[son][0]+len>dp[root][0])
                {
                    dp[root][1]=dp[root][0];
                    myson[root]=son;
                    dp[root][0]=dp[son][0]+len;
                }
                else if(dp[son][0]+len>dp[root][1])
                {
                    dp[root][1]=dp[son][0]+len;
                }
                vis[son]=false;
            }
        }
    }

    void dfs2(int root)
    {
        for(int i=0;i<(int)vec[root].size();++i)
        {
            int son = vec[root][i].first;
            int len = vec[root][i].second;
            if(!vis[son])
            {
                if(myson[root]==son)
                    dp[son][2]=max(dp[root][2],dp[root][1])+len;
                else
                    dp[son][2]=max(dp[root][2],dp[root][0])+len;
                vis[son]=true;
                dfs2(son);
                vis[son]=false;
            }
        }
    }

    int PointsOnDiameter(int n, vector<int>& u, vector<int>& v) {
        // write code here
        int m = u.size();
        for(int i=0;i<m;++i)
        {
            vec[u[i]].push_back(make_pair(v[i],1));
            vec[v[i]].push_back(make_pair(u[i],1));
        }
        for(int i=1;i<=n;++i){
            vis[i]=false;
            dp[i][0]=dp[i][1]=dp[i][2]=0;
            myson[i]=0;
        }
        vis[1]=true;
        dfs1(1);
        dfs2(1);
        vis[1]=false;
        int mx = 0;
        for(int i=1;i<=n;++i)
            mx=max(mx,dp[i][0]+dp[i][2]);
        int ans = 0;
        for(int i=1;i<=n;++i)
        {
            if(dp[i][0]+dp[i][1]+dp[i][2]-min(dp[i][0],min(dp[i][1],dp[i][2]))==mx)
                ans++;
        }
        return ans;
    }
};
*/