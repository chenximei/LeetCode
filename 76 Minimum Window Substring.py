class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # 第一步，将  要寻找的被包含信息存放到字典中
        dic = {}
        for i in t:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1

        #  定义好指针和变量
        start = 0
        minlen = len(s)
        cnt = 0
        result = ""
        for i in range(len(s)):

            # 一个启动条件，当现在走到的字符在  目标字符 中时，我们再进行考虑。  这里for的遍历其实就相当于一种right的右移。
            if (s[i] in t):
                dic[s[i]] -= 1
                #对出现情况进行统计，在这个范围内有合适的累计
                if dic[s[i]] >= 0:
                    cnt += 1

                #核心的，当我们发现现在是合法合理时，就可以考虑  对于left和right指针进行左移和右移的问题，先left左移，一直到不满足条件为止吧
                while (cnt == len(t)):

                    # 重要的 当找到新的最小窗口时，思考进行结果的保存
                    if (i - start + 1) <= minlen:
                        minlen = i - start + 1
                        result = s[start:i + 1]

                    #进行start和end的调整，让start往前缩
                    start += 1
                    if s[start - 1] in t:
                        dic[s[start - 1]] += 1
                        if dic[s[start - 1]] > 0:
                            cnt -= 1
        return result

if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    solution = Solution()
    res = solution.minWindow(S,T)
    print(res)

