# To generate all n-pair parentheses, we can do the following:
#
# Generate one pair: ()
#
# Generate 0 pair inside, n - 1 afterward: () (...)...
#
# Generate 1 pair inside, n - 2 afterward: (()) (...)...
#
# ...
#
# Generate n - 1 pair inside, 0 afterward: ((...))

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]] # 每一次x是在括号内加从0开始轮，y是从i前边那个开始轮，最后互相到头
                #动态规划体现为，n等于1的时候，先创建一个括号，n再上升的时候，即每次多加一个括号，然后在括号内和括号外分别循环加入前面所有的组合
        return dp[n]


if __name__ == '__main__':
    n = 3
    solution = Solution()
    res = solution.generateParenthesis(n)
    print(res)
