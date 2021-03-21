# include <stdio.h>
# include <algorithm>
# include <string.h>
# include <math.h>


using namespace std;
typedef long long LL;

const int max_n = 100020;

struct point{
    int x, y;
    point() {};
    point(int _x, int _y) {
        x = _x;
        y = _y;
    }
}p[max_n];

bool cmp_x(const point& A, const point& B)
{
    return A.x < B.x;
}

bool cmp_y(const point& A, const point& B)
{
    return A.y < B.y;
}

LL cal_dis(int x1, int y1, int x2, int y2)
{
    return (LL) abs(x1-x2)+abs(y1-y2);
}


int main()
{
    int T, t;
    int x, y, bias, n;
    LL ans;
    pair<int, int> mid_p;
    scanf("%d", &T);
    for(int t = 1; t <= T;t++) {
        ans = 0;
        scanf("%d", &n);
        for (int i = 0;i < n;i++) {
            scanf("%d%d", &x, &y);
            p[i].x = x;
            p[i].y = y;
        }
        sort(p, p+n, cmp_x);
        for (int i = 0;i < n;i++) {
            p[i].x -= i;
        }

        sort(p, p+n, cmp_y);
        mid_p.second = p[n/2].y;
        sort(p, p+n, cmp_x);
        mid_p.first = p[n/2].x;
        //printf("mid point -> (%d, %d)\n", mid_p.first, mid_p.second);
        for (int i = 0;i < n;i++) {
            ans += cal_dis(p[i].x, p[i].y, mid_p.first, mid_p.second);
        }

        printf("Case #%d: %lld\n", t, ans);
    }
}
/*
2
2
1 1
4 4
3
1 1
1 2
1 3
*/