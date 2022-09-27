class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


nums = [2,3,1,2,4,2,3]
solution = Solution()
res = solution.jump(nums)
print(res)

