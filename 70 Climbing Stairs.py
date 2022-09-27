#斐波那契数列，公式：f(n) = f(n - 1) + f(n - 2)
#斐波那契数列：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233……
#第一项和第二项是1，之后的每一项为之前两项的和。
#假设有3级台阶，先爬1阶，接下来还有2阶台阶，那问题就是有2阶台阶怎么爬，先爬2阶，接下来还有1阶台阶，那问题就是有1阶台阶怎么爬
#假设有4级台阶，先爬1阶，接下来还有3阶台阶，那问题就是有3阶台阶怎么爬，先爬2阶，接下来还有2阶台阶，那问题就是有2阶台阶怎么爬
#假设有n级台阶，先爬1阶，接下来还有 n - 1 阶台阶，那问题就是有n - 1阶台阶怎么爬，先爬2阶，接下来还有 n - 2 阶台阶，那问题就是有n - 2阶台阶怎么爬


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return [1, 2][n - 1]
        first = 1
        second = 2
        cnt = 2
        while cnt < n:
            cnt += 1
            cur = first + second
            if cnt == n:
                return cur
            first = second
            second = cur

if __name__ == '__main__':
    n = 8
    solution = Solution()
    res = solution.climbStairs(n)
    print(res)