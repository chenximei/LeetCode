class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0 #start 到 i 是目前的小窗口，没有重复字符的
        usedChar = {}

        for i, c in enumerate(s):
            if c in usedChar and start <= usedChar[c]: #如果出现重复字符，而且滑窗起始点小于等于重复字符的index
                start = usedChar[c] + 1 #将滑窗从重复字符的index处后移一位，保持滑窗内没有重复字符
            else:
                maxLength = max(maxLength, i - start + 1) #计算当前最长无重复长度，譬如说前三个abc，长度是（2-0）+ 1 = 3

            usedChar[c] = i #字典记录的是，当前key值最后一次出现的index位置，为了以后更新start用

        return maxLength

if __name__ == '__main__':
    s = "abcabcbbdefg"
    solution = Solution()
    res = solution.lengthOfLongestSubstring(s)
    print(res)