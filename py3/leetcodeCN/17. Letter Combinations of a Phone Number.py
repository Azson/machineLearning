class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []

        dt = {
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        def func(s1, ans, now):
            if len(s1) == 0:
                if len(now) != 0:
                    ans.append(now)
                #print('add {0}'.format(now))
                return

            if s1[0] < '7':
                for i in range(3):

                    ch = chr(ord('a') + (int(s1[0]) - 2) * 3 + i)

                    func(s1[1:], ans, now + ch)
            else:
                for ch in dt[s1[0]]:
                    func(s1[1:], ans, now+ch)

        func(digits, ans, '')

        return ans
