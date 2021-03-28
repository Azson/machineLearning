class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        ans = 0
        st = set()
        now = 0
        for i in range(len(word)):
            if (word[i] >= '0' and word[i] <= '9'):
                now = now*10 + int(word[i]) - int('0')
            else:
                if (i and word[i-1] >= '0' and word[i-1] <= '9'):
                    st.add(now)
                    now = 0
        if (word[-1] >= '0' and word[-1] <= '9'):
                st.add(now)
        return len(st)