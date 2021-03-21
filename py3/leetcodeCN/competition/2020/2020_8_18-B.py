v, k = list(map(int, input().split(' ')))

mod = int(1e9+7)



f = 0
if k > v:
    f = k-v
    k = v
v //= 2
k = k//2 -1

ans = [1]*k


while k < v-1:
    k += 1
    ans.append(0)

ans.append(1)

ret = 0

for i in ans[::-1]:
    ret = (ret*2 %mod + i) % mod

for i in ans:
    ret = (ret*2 %mod + i) % mod
print(ans, f, ret)
while f > 0:
    f -= 1
    ret = (ret*2 %mod + 1) % mod

print(ret)

