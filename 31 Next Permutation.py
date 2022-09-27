#寻找下一个更大的数
#（1）首先是 从后往前找到第一个产生降序的数字，然后将这个数字位替换成其后面中稍微比其大一个的数字。
#（2）然后对于后面剩余的位数进行排序即可，这样的操作就能够实现获取得到在数字排序角度找到稍微更大一点的数字。

class Solution:
    def nextPermutation(self, nums) -> None:
        i = len(nums) - 2 #让倒数第二个和倒数第一个对比

        # while i>=0:  这样写是错的，因为while只是循环，不管i的增减，如果if不成立，那就陷入死循环
        #     if nums[i] >= nums[i+1]:
        #         i -= 1

        while i >= 0 and nums[i] >= nums[i + 1]: #从右往左数，如果一直是升序则再往左找，直到找到第一个降序的数
        # 这样写如果条件不成立就直接结束，因为while是循环+条件语句，如果条件不成立就结束
            i -= 1
        if i >= 0:
            j = len(nums) - 1 #再次从右往左找，找到第一个比之前降序数大的
            while j >= 0 and nums[i] >= nums[j]: #如果写成 while j > i and nums[i] > nums[j]是错的，如果i和j是相等的就不成立，
                # j不能继续往前移动去寻找比i大的数
                j -= 1
            nums[i], nums[j] = nums[j], nums[i] #交换两个数，注意，交换两个数之后，i位置之后的数依然是降序

        left, right = i + 1, len(nums) - 1 #下面是排序，将交换后的i位置之后的数从小到大排序，因为后面的数是降序的，所以倒置排序即可
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums

nums = [1,5,1]
solution = Solution()
next = solution.nextPermutation(nums)
print(next)