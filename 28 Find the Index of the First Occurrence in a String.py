#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 24.09.22 9:07 PM
# @Author  : Chen Jinwei
# @FileName: 28 Find the Index of the First Occurrence in a String.py

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        slow = 0
        fast = 0
        i = 0

        if len(needle) > len(haystack):
            return -1

        while (fast < len(haystack)):
            temp = fast # 先保存出发点的值，之后会用这个的下一位做新的出发点
            while (i < len(needle)):
                if fast < len(haystack) and needle[i] == haystack[fast]:    # 一定加上判断fast是否超出范围的条件，如果匹配过程中走到了haystack外，
                    # 则不能继续匹配，而且这个条件一定要写在判断相等的前面，因为fast不合理的时候不能用，得先判断fast是否合理
                    if i == len(needle) - 1:
                        return slow # 只找第一个，直接返回
                        # slow = fast + 1
                        # i += 1
                    else:
                        i += 1
                        fast += 1
                else:
                    break
            fast = temp + 1 # 不能fast在匹配过程中，匹配一半不合理就从不合理的地方接着往下走，得回到刚才起点的下一位再找，
            # 因为那一半不合理的里面，也可能有合理的开头，不能错过开头
            slow = fast # slow和fast在从新的一点出发开始找的时候，要保持出发点一致
            i = 0   # 把i归零，因为needle要从头开始判断

        return -1

    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m,n=len(haystack),len(needle)
        for i in range(m):
            if haystack[i:i+n]==needle:
                return i
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        next = self.getnext(a, needle)
        p = -1
        for j in range(b):
            while p >= 0 and needle[p + 1] != haystack[j]:
                p = next[p]
            if needle[p + 1] == haystack[j]:
                p += 1
            if p == a - 1:
                return j - a + 1
        return -1

    def getnext(self, a, needle):
        next = ['' for i in range(a)]
        k = -1
        next[0] = k
        for i in range(1, len(needle)):
            while (k > -1 and needle[k + 1] != needle[i]):
                k = next[k]
            if needle[k + 1] == needle[i]:
                k += 1
            next[i] = k
        return next

solution = Solution()
haystack = "mississippi"
needle = "issipi"
res = solution.strStr2(haystack,needle)
print(res)
