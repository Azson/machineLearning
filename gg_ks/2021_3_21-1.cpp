# include <cstdio>
# include <vector>
# include <string>
# include <cstring>
# include <algorithm>
# include <stack>
# include <queue>
# include <set>
# include <iostream>

using namespace std;

typedef long long LL;

using namespace std;


int main() {

    int T, n, K, score;
    string str;
    scanf("%d", &T);
    for (int cas = 1;cas <= T;cas++) {
        scanf("%d%d", &n, &K);
        cin >> str;
        score = 0;
        for (int i = 0;i < n/2;i++) {
            if (str[i] != str[n-i-1]) {
                score ++;
            }
        }
        score = abs(score-K);
        printf("Case #%d: %d\n", cas, score);
    }
    return 0;
}
/*
2
5 1
ABCAA
4 2
ABAA

*/