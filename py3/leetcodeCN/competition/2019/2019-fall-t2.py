class Solution(object):
    def fraction(self, cont):
        """
        :type cont: List[int]
        :rtype: List[int]
        """
        ln = len(cont)
        if ln == 1:
            return [cont[0], 1]

        def gcd(x, y):
            return gcd(y, x % y) if y else x

        fz = 1
        fm = cont[-1]
        for idx in range(ln - 2, 0, -1):
            tmp = fz
            fz = fm
            fm = cont[idx] * fm + tmp
            # print("{0} , fz {1} / {2}".format(idx, fz, fm))
            tmp = gcd(fz, fm)
            fz //= tmp
            fm //= tmp

        fz += cont[0] * fm

        tmp = gcd(fz, fm)
        # print(fz, fm, tmp)
        return [fz // tmp, fm // tmp]