########    第一种.回溯的方式    ##########
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, tmp = [], []

        def generate(nums, n):
            res.append(tmp[:])

            if n == len(nums):
                return
            for i in range(n, len(nums)):
                tmp.append(nums[i])
                n += 1
                generate(nums, n)
                tmp.pop()

        generate(nums, 0)
        return res

########    第二种.线性搜索的方式    ##########
class Solution1(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            for i in result[:]:
                item = i[:]
                item.append(num)
                result.append(item[:])
        return result

if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    solution1 = Solution1()
    res = solution.subsets(nums)
    print(res)

