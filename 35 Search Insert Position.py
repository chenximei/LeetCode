class Solution:
    def searchInsert(self, nums, target) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low # 假如没找到的话，low的位置将会是刚刚处在比target大一点点的位置，即target将要插入的位置，譬如说在[1,3,5,6]里找2，2需要被插入在1号位置
        # 循环中先是 0，1，3，然后变成0，0，0，然后变成1，0，0，最后是low在符合插入的位置


nums = [1,3,5,6]
target = 2
solution = Solution()
index = solution.searchInsert(nums,target)
print(index)
