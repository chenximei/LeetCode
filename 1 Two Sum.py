from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

if __name__ == '__main__':
    nums = [7,1,2,5,4,2,6]
    target = 13
    solution = Solution()
    res = solution.twoSum(nums,target)
    print(res)