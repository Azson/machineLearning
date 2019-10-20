class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """

        mp = {}
        folder = sorted(folder)
        for idx, item in enumerate(folder):

            ret = item.split('/')
            ln = len(ret)
            for i in range(2, ln+1):
                now = '/'.join(ret[:i])
                if now in mp:
                    print("idx {0}, now {1}".format(idx, now))
                    break
                if i == ln:
                    mp[item] = True

        return list(mp.keys())


if __name__ == '__main__':


    ls = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    ls2 = ["/a","/a/b/c","/a/b/d"]
    ls3 = ["/a/b/c","/a/b/d","/a/b/ca"]
    obj = Solution()
    print(obj.removeSubfolders([]))