# include <stack>

using namespace std;

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> qe;
        int n = pushed.size();
        for (int i = 0, j = 0;i < n;i++) {
            qe.push(pushed[i]);
            while (qe.top() == popped[j]) {
                qe.pop();
                j ++;
            }
        }
        return j == n;
    }
};