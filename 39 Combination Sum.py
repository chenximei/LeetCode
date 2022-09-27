from typing import List
class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, nums, target, path, res): #如果dfs在conbi函数下面，则引用时不写self.，但使用时要加上self内参
        # if target < 0:
        #     return
        if target == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            if nums[i] > target:  # here
                continue #用break会出错，在某些输入的情况下
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], res) #注意是path + [nums[i]]

candidates = [2,3,6,7]
target = 7
solution = Solution()
res = solution.combinationSum(candidates,target)
print(res)