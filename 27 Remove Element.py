#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 21.09.22 9:13 AM
# @Author  : Chen Jinwei
# @FileName: 27 Remove Element.py

class Solution:
    def removeElement(self, nums, val: int) -> int:
        if nums is None or len(nums)==0:
            return 0
        l=0
        r=len(nums)-1
        while l<r:
            while(l<r and nums[l]!=val):
                l+=1
            while(l<r and nums[r]==val):
                r-=1
            nums[l], nums[r]=nums[r], nums[l]
        print(nums)
        if nums[l]==val:
            return l
        else:
            return l+1

    def removeElement1(self, nums, val):
        if nums is None or len(nums) == 0: # 排除数组为空
            return 0
        l = 0   # 只需设置l是0
        for r in range(len(nums)):
            if(l <= r and nums[r] != val): # 如果快指针碰到不是val的时候，慢指针才跟着动
                nums[l] = nums[r]
                l+=1    # 因为到最后，慢指针又走了一步，但是快指针不走了，所以最后l指向比剩下真正要留下的数组的最后一位的再后面一个，所以l的index是size
        return l

