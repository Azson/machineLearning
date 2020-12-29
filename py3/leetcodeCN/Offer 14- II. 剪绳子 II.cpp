class Solution {
public:
    typedef long long LL;
    LL mod = 1000000007;
    int cuttingRope(int n) {
        if (n <= 3)
            return n-1;
        int a, b;
        LL ans = 1, c = 3;
        a = n / 3 - 1;
        b = n % 3;
        while (a > 0) {
            if (a&1) ans = (ans*c) % mod;
            c = c*c %mod;
            a >>= 1;
        }
        if (b == 1) {
            return ans*4 %mod;
        }
        else if (b == 2) {
            return ans*6 %mod;
        }
        return ans*3 %mod;
    }
};