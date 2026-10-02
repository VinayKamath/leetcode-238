# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:52:30 2026

@author: vinay
"""
from typing import List

def productExceptSelf(nums: List[int])->List[int]:
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
                
        result.append(product)
    
    return result
    
nums = [1, 2, 4, 6]
productExceptSelf(nums)