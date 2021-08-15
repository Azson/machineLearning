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
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int> > pqe;
        for (auto & x : nums) {
            if (pqe.size() < k) {
                pqe.push(x);
            }
            else if (pqe.top() < x) {
                pqe.pop();
                pqe.push(x);
            }            
        }
        return pqe.top();
    }
};


int main() {

    return 0;
}