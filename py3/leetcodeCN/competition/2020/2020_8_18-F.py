def dfs(u, c):
    for v in graph[u]:
        if color[v] == c:
            ans = 1
            return
        if color[v] == -c:
            continue
        color[v] = -c
        dfs(v, -c)



max_n = 100000+5
import sys
sys.setrecursionlimit(max_n)

n, m = list(map(int, input().split(' ')))

graph = {i:[] for i in range(max_n)}
color = [0] * (max_n)
for i in range(m):
    u, v = list(map(int, input().split(' ')))
    graph[u].append(v)
    graph[v].append(u)

color[1] = 1
ans = 0
dfs(1, 1)

if n == 1:
    print(1)
elif ans == 0:
    print(2)
else:
    print(3)


