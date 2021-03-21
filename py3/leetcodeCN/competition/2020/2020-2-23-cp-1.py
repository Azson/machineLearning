#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
# @ModuleName : 2020-2-23-cp-1
# @Function : 
# @Author : azson
# @Time : 2020/2/23 10:28
'''


class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """

        def split_date(date):
            return list(map(lambda x:int(x), date.split('-')))

        def count_days(date):
            ret = days[date[1] - 1] + date[2]
            if (((date[0] % 4 == 0 and date[0] % 100 != 0) or date[0] % 400 == 0) and date[1] > 2):
                ret += 1
            return ret

        days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

        new_date_1 = split_date(date1)
        new_date_2 = split_date(date2)

        day1 = count_days(new_date_1)
        day2 = count_days(new_date_2)

        if new_date_1[0] == new_date_2[0]:
            return abs(day1-day2)

        if new_date_1[0] > new_date_2[0]:
            day1, day2 = day2, day1
            new_date_1, new_date_2 = new_date_2, new_date_1

        ans = 366 if ((new_date_1[0] % 4 == 0 and new_date_1[0] % 100 != 0) or new_date_1[0] % 400 == 0) else 365
        for y in range(new_date_1[0]+1, new_date_2[0]):

            ans += 366 if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0) else 365
        ans = ans-day1+day2

        return ans


if __name__ == '__main__':

    obj = Solution()
    date1="1971-06-29"

    date2="2010-09-23"
    print(obj.daysBetweenDates(date1, date2))