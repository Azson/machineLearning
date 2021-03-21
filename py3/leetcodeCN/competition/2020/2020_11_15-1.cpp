# include <stdio.h>
# include <algorithm>


using namespace std;

int main()
{
    int T, t;
    int n, k, s, ans;
    scanf("%d", &T);
    for(int t = 1; t <= T;t++) {
        ans = 0;
        scanf("%d%d%d", &n, &k, &s);
        ans += k-1+(n-s+1);
        ans += min(k-s, s);
        printf("Case #%d: %d\n", t, ans);
    }
}