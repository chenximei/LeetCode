class Solution:
    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 定义状态数组.  每个状态的含义都是 最小的组成数字
        dp = [0] * (n + 1)

        # 进行状态上的计算转移。就像贝诺蔓塔一样的不断累上算。
        for i in range(1, n + 1):
            dp[i] = i  # 最坏情况是加1，也就是所有1加一起，我们的目标当然是最少比较好
            # 尝试更新，减少那种累计数字
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]

if __name__ == '__main__':
    n = 13
    solution = Solution()
    res = solution.numSquares1(n)
    print(res)