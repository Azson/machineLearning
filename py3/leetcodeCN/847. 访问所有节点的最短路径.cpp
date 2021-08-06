# include <cstdio>
# include <vector>
# include <algorithm>
# include <queue>


using namespace std;
// cost, path, node
#define triple pair<int, pair<int, int> >

class Solution {
public:
    int ans = 0;
    int n;
    vector<vector<bool> > dp;

    int shortestPathLength(vector<vector<int>>& graph) {
        n = graph.size();
        dp.resize(n, vector<bool> (1 << n, false));
        queue<tuple<int, int, int> > pqe;
        for (int i = 0;i < n;i++) {
            pqe.emplace(0, 1 << i, i);
        }
        
        triple now;
        int u, path;
        while (!pqe.empty()) {
            auto [c, path, u] = pqe.front();
            pqe.pop();

            

            if (path == (1 << n) - 1) {
                ans = c;
                break;
            }
            for (int& v : graph[u]) {
                int tmp = path | (1 << v);
                if (dp[v][tmp]) {
                    continue;
                }
                pqe.emplace(c+1, tmp, v);
                dp[v][tmp] = true;
            }
        }
        return ans;
    }
};


int main() {

    return 0;
}