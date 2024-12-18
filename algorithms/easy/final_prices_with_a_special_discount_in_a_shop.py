# 1475. Final Prices With a Special Discount in a Shop

from typing import List

def finalPrices(self, prices: List[int]) -> List[int]:
    output, stack = prices.copy(), []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[i]:
            j = stack.pop()
            output[j] -= prices[i]

        stack.append(i)

    return output