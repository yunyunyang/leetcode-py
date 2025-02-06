# 1726. Tuple with Same Product

from typing import List

def tupleSameProduct(self, nums: List[int]) -> int:
    product = {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            key = nums[i] * nums[j]
            product[key] = product.get(key, 0) + 1
    
    res = 0
    for val in product.values():
        if val >= 2:
            comb = ((val - 1) * val) // 2
            res += comb * 8

    return res