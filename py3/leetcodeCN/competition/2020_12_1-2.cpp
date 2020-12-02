# include <cstdio>
# include <algorithm>
# include <string>
# include <stack>



using namespace std;


typedef long long LL;
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 给定一个后缀表达式，返回它的结果
     * @param str string字符串 
     * @return long长整型
     */
    long long solve(string str) {
        // write code here
        stack<LL> num;
        stack<char> op;
        int n = str.length();
        LL tmp, k, ans;
        int f = 0;
        char c;
        for (int i = 0;i < n;) {
            if (str[i] >= '0' && str[i] <= '9') {
                tmp = 0;
                while (str[i] != '#') {
                    tmp = tmp*10 + str[i]-'0';
                    i ++;
                }
               
                num.push(tmp);
            }
            if (str[i] == '+') {
                tmp = num.top();
                num.pop();
                k = num.top();
                num.pop();
                num.push(tmp+k);
            }
            if (str[i] == '-') {
                tmp = num.top();
                num.pop();
                k = num.top();
                num.pop();
                num.push(k-tmp);
            }
            if (str[i] == '*') {
                tmp = num.top();
                num.pop();
                k = num.top();
                num.pop();
                num.push(tmp*k);
            }
             i++;
        }
        return num.top();
    }
};


int main()
{
    Solution obj = Solution();
    // "1#1#+"
    // "12#3#+15#*"
    // "1#12#-"
    printf("%lld\n", obj.solve("12#3#+7#3#+*"));
    return 0;
}