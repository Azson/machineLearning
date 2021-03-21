# include <stdio.h>
# include <vector>

using namespace std;

const int max_n = 100000+5;
vector<int> graph[max_n];
int color[max_n];
int ans = 0;

void dfs(int u, int c) 
{
    int v;
    for (int i = 0;i < (int)graph[u].size();i++) {
        v = graph[u][i];
        if (color[v] == c) {
            ans = 1;
            return ;
        }
        if (color[v] == -c) continue;
        color[v] = -c;
        dfs(v, -c);
    }
}

int main()
{
    int n, m, u, v;
    scanf("%d %d", &n, &m);
    for(int i = 0;i < m;i++) {
        scanf("%d %d", &u, &v);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    color[1] = 1;
    dfs(1, 1);

    if (n == 1) 
        printf("1\n");
    else if(ans == 0)
        printf("2\n");
    else
    {
        printf("3\n");
    }
    
    return 0;
}
