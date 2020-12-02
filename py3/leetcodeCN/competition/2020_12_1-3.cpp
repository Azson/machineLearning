# include <cstdio>
# include <vector>

using namespace std;


class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 
     * @param e int整型vector 长度为n-1的数组，表示结点2到结点n的父结点
     * @return int整型
     */
    const static int N = 1e5+10;
    vector<int> G[N];
    int dis[N], n;
    int dfs(int u, int pre) {
        dis[u] = dis[pre] + 1;
        int mx = dis[u];
        for (auto& v : G[u]) {
            if (v != pre) {
                mx = max(mx, dfs(v, u));
            }
        }
        return mx;
    }
    int get_mx(int mx) {
        for (int i = 1;i <= n;i++) {
            if (dis[i] == mx) {
                return i;
            }
        }
        return 0;
    }
    int get_sec() {
        vector<int> tmp(2, 0);
        for (int i = 1;i <= n;i++) {
            if (dis[i] > tmp[0]) {
                tmp[1] = tmp[0];
                tmp[0] = dis[i];
            }
            else if (dis[i] > tmp[1]) {
                tmp[1] = dis[i];
            }
        }
        return tmp[1];
    }
    int tree3(vector<int>& e) {
        // write code here
        
        n = e.size()+1;
        for (int i = 1;i <= n+1;i++)    G[i].clear();
        for (int i = 2;i <= n;i++) {
            G[i].push_back(e[i-2]);
            G[e[i-2]].push_back(i);
        }

        int mx = dfs(1, 0);
        int p = get_mx(mx);
        //get_sec();
        mx = dfs(p, 0);
        p = get_mx(mx);
        int t1 = get_sec();
        mx = dfs(p, 0);
        int t2 = get_sec();
        return max(t1, t2) - 1;
    }
};

int main(int argc, char const *argv[])
{
    Solution obj = Solution();
    vector<int> ip(4);
    ip[0] = 1;ip[1] = 2;ip[2] = 3;ip[3] = 4;
    printf("%d\n", obj.tree3(ip));
    return 0;
}
