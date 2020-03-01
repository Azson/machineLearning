class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        record = dict()
        people = len(votes[0])
        for item in votes:
            for idx, char in enumerate(item):
                if char not in record:
                    record[char] = [0]*people
                record[char][idx] += 1

        import functools
        def is_better(x, y):
            for rk in range(people):
                if x[1][rk] != y[1][rk]:
                    return -1 if x[1][rk] > y[1][rk] else 1
            return -1 if x[0] < y[0] else 1


        ret = sorted(list(record.items()), key=functools.cmp_to_key(is_better))
        ans = [x[0] for x in ret]

        return ''.join(ans)



if __name__ == '__main__':
    obj = Solution()
    votes =  ["ABC","ACB","ABC","ACB","ACB"]
    print(obj.rankTeams(votes))