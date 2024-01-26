from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind1, i in enumerate(nums):
            for ind2, el in enumerate(nums):
                if ind1 == ind2:
                    break
                d = i + el
                if d == target:
                    nums = [ind1, ind2]
                    return nums
