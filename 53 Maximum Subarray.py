class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        这是之前  被问过的一道题。
            这里的核心思想就在于语句：max(dp[i-1] + nums[i], nums[i])
            我们需要的最大的，也就是如果新加入的数 还不如不加，我们保存之前最大的即可，然后继续往后走。我们以res保存最终要保留的最大字序和。
            这里使用max的原因是 如果之前的加上当前的比 当前的还小， 那就保留当前的即可，否则就用 之前+当前标识  标识考虑当前情况下的最大 即可。
        """
        if not nums:
            return 0
        dp = [nums[0]]
        res = dp[0]
        for i in range(1, len(nums)):
            dp.append(max(dp[i-1] + nums[i], nums[i]))
            if dp[-1] > res:
                res = dp[-1]
        return res

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    res = solution.maxSubArray(nums)
    print(res)
