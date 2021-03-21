# include <stdio.h>
# include <algorithm>
# include <math.h>


using namespace std;
typedef long long LL;
int a[30];

LL count_boring(LL x)
{
    if (x <= 0)
        return 0;
    LL ans = 0;
    int ln = 0;
    while (x) {
        a[ln++] = x % 10;
        x /= 10;
    }
    if (ln > 1) {
        ans += (LL) (pow(5, ln-1)-1) / 4 * 5;
    }
    for (int i = ln-1;i >= 0;i--) {
        
        for (int j = 0;j < a[i];j++) {
            if (!j && i==ln-1)  continue;
            if ((ln-i) % 2 != j % 2 )
                continue;
            ans += pow(5, i);
        }
        if ((ln-i) % 2 != a[i] % 2 )
            break; 
        if (!i && ln%2 == a[i] % 2) 
            ans ++;
    }
    return ans;
}

int main()
{
    int T, t;
    LL l, r, ans;
    scanf("%d", &T);
    for(int t = 1; t <= T;t++) {
        ans = 0;
        scanf("%lld%lld", &l, &r);
        ans = count_boring(r) - count_boring(l-1);
        //printf("%lld -> %lld, %lld -> %lld\n", l-1, count_boring(l-1), r, count_boring(r));
        printf("Case #%d: %lld\n", t, ans);
    }
}
/*
3
5 15
120 125
779 783
*/