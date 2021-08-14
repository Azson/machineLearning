# include <cstdio>
# include <stack>
# include <vector>
# include <algorithm>
# include <queue>
# include <cstring>
# include <map>

using namespace std;
class Solution {
public:
    int find_index(int u, int target, vector<vector<int>>& preferences, int& n) {
        for (int i = 0;i < n;i++) {
            if (preferences[u][i] == target) {
                return i;
            }
        }
        return -1;
    }
    bool is_happy(int u, int v, vector<vector<int>>& preferences, int& n, int* mp) {
        int v_idx = find_index(u, v, preferences, n);
        for (int i = 0;i < v_idx;i++) {
            int u_idx = find_index(preferences[u][i], u, preferences, n);
            int y_idx = find_index(preferences[u][i], mp[preferences[u][i]], preferences, n);
            // printf("handle (%d, %d) index %d -- another (%d) index (%d, %d) ans\n", u, v, v_idx, preferences[u][i], u_idx, y_idx);
            if (u_idx < y_idx) {
                return false;
            }
        }
        return true;
    }
    int unhappyFriends(int n, vector<vector<int>>& preferences, vector<vector<int>>& pairs) {
        int ans = 0;
        int mp[510];
        int u, v;
        for (int i = 0;i < n/2;i++) {

            u = pairs[i][0];
            v = pairs[i][1];
            mp[u] = v;
            mp[v] = u;
        }
        for (auto & pr : pairs) {
            u = pr[0];
            v = pr[1];
            if (preferences[u][0] != v && !is_happy(u, v, preferences, n, mp)) {
                ans ++;
            }
            if (preferences[v][0] != u && !is_happy(v, u, preferences, n, mp)) {
                ans ++;
            }
        }
        return ans;
    }
};


int main() {

    return 0;
}