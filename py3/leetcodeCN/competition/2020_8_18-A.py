n, m = list(map(int, input().split(' ')))

T = []
S = []
cute = [0]*n
for i in range(n):

    T.append(input())
    
for i in range(m):
    s = input()
    for j in range(n):
        f = False
        st = 0
        for k in T[j]:
            if s[st] == k:
                st += 1
                if st == len(s):
                    f = True
                    break
        if f:
            cute[j] += 1

for i in range(n):
    print(cute[i])