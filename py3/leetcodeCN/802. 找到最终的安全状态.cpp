# include <cstdio>
# include <vector>
# include <algorithm>
# include <queue>


using namespace std;


class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> deg(n);
        vector<vector<int> > out(n);
        for (int i = 0;i < n;i++) {
            for (int& v : graph[i]) {
                out[v].push_back(i);
                deg[i] ++;
            }
        }
        queue<int> pqe;
        for (int i = 0;i < n;i++) if (!deg[i]) {
            pqe.push(i);
        }
        int now;
        vector<int> ans;
        while (!pqe.empty()) {
            now = pqe.front();
            pqe.pop();

            ans.push_back(now);
            for (int& v : out[now]) {
                deg[v] --;
                if (deg[v] == 0) {
                    pqe.push(v);
                }
            }
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};

int main() {

    // vector<int> vec = {1,1,3,4};
    // Solution so = Solution();
    // printf("%d\n", so.triangleNumber(vec));
}