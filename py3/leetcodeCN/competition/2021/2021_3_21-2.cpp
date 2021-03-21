# include <cstdio>
# include <vector>
# include <string>
# include <cstring>
# include <algorithm>
# include <stack>
# include <queue>
# include <set>
// # include < prio

using namespace std;

typedef long long LL;

typedef pair<int, int> P;

class Solution {
public:
    int getNumberOfBacklogOrders(vector<vector<int> >& orders) {
        priority_queue<P, vector<P>, greater<P> > sell;
        priority_queue<P, vector<P>, less<P> > buy;
        P tmp;
        for (vector<int>& order : orders) {
            if (order[2] == 0) {
                while (!sell.empty() && sell.top().first <= order[0]) {
                    tmp = sell.top();
                    sell.pop();
                    if (tmp.second > order[1]) {
                        tmp.second -= order[1];
                        sell.push(tmp);
                        order[1] = 0;
                        break;
                    }
                    else {
                        order[1] -= tmp.second;
                    }
                }
                // cout << "buy: " << order[0] << ' ' << order[1] << endl;
                if (order[1] > 0) {
                    
                    buy.push(make_pair(order[0], order[1]));
                }
                    
            }
            else {

                while (!buy.empty() && buy.top().first >= order[0]) {
                    tmp = buy.top();
                    buy.pop();
                    if (tmp.second > order[1]) {
                        tmp.second -= order[1];
                        buy.push(tmp);
                        order[1] = 0;
                        break;
                    }
                    else {
                        order[1] -= tmp.second;
                    }
                }
                // cout << "sell: " << order[0] << ' ' << order[1] << endl;
                if (order[1] > 0) {
                    
                    sell.push(make_pair(order[0], order[1]));
                }
            }
        }
        LL ans = 0;
        LL mod = 1e9+7;
        
        while (!sell.empty()) {
            tmp = sell.top();
            ans = (ans + tmp.second) %mod;
            sell.pop();
        }
        while (!buy.empty()) {
            tmp = buy.top();
            ans = (ans + tmp.second) %mod;
            buy.pop();
        }
        return ans;
    }
};


int main() {

    return 0;
}