#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 24.09.22 10:21 AM
# @Author  : Chen Jinwei
# @FileName: 18 4Sum.py

class Solution:
    def fourSum(self, nums, target: int):

        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for k in range(i + 1, n):
                if k > i + 1 and nums[k] == nums[k - 1]: continue   # 注意这里一定是k > i+1，而不是k>0，
                # 因为譬如说测试用例是[2,2,2,2,2]这种情况，因为允许结果中有相等的数，但是不同结果不能互相相同，如果用k>0，那判断nums[1]==nums[0]，
                # 因为1和0相等就跳过了，之后也会一直跳过。
                p = k + 1
                q = n - 1

                while p < q:
                    if nums[i] + nums[k] + nums[p] + nums[q] > target:
                        q -= 1
                    elif nums[i] + nums[k] + nums[p] + nums[q] < target:
                        p += 1
                    else:
                        res.append([nums[i], nums[k], nums[p], nums[q]])
                        while p < q and nums[p] == nums[p + 1]: p += 1
                        while p < q and nums[q] == nums[q - 1]: q -= 1
                        p += 1
                        q -= 1
        return res