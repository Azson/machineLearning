class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """

        cnt = [0] * 4
        sum = [[0]*(len(s)+1) for i in range(4)]
        mp = {
            'Q' : 0,
            'W' : 1,
            'E' : 2,
            'R' : 3
        }
        for idx, item in enumerate(s):
            cnt[mp[item]] += 1
            for i in range(4):
                sum[i][idx+1] = sum[i][idx]
            sum[mp[item]][idx + 1] += 1

        banlance = len(s) // 4
        cnt = [item - banlance for item in cnt]

        if cnt[0] == 0 and cnt[0] == cnt[1] and cnt[0] == cnt[2] \
                and cnt[0] == cnt[3]:
            return 0
        print(cnt, sum)
        ans = 0
        for ln in range(1, len(s)):
            for st in range(0, len(s)-ln+1):
                #print(st, ln)
                f = True
                for ch in range(4):
                    if cnt[ch] > 0:
                        if sum[ch][st+ln] - sum[ch][st] != cnt[ch]:
                            f = False
                            #print("ch {0} fail~ sum {1} ~ {2}".format(ch, sum[ch][st], sum[ch][st+ln]))
                            break

                if f:
                    ans = ln
                    break
            if ans != 0:
                #print("find!~")
                break
        return ans



if __name__ == '__main__':

    s1 = "QQQQ"
    s2 = "WQWRQQQW"
    obj = Solution()

    print(obj.balancedString(s2))