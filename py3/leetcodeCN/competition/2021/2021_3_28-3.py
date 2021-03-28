class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        words = list(filter(lambda x:len(x) > 0, s.replace('(', ' ').replace(')', ' ').split(' ')))
        mp = dict()
        vis = dict()
        num = 0
        for i in range(len(s)):
            if (s[i] == '('):
                vis[num] = True
                
                num += 1
            elif (s[i] == ')'):
                if (i+1 != len(s) and s[i+1] != '('):
                    num += 1
            elif (i == 0):
                num += 1
        for key, val in knowledge:
            mp[key] = val
        for i in range(len(words)):
            if (i not in vis):
                continue
            if (words[i] in mp):
                words[i] = mp[words[i]]
            else:
                words[i] = '?'
        return ''.join(words)
        