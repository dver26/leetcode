from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            print(f"Ciclo {i}")
            for j in range(len(nums)):
                print(j)
                print(f"n1: {nums[i]} + n2: {nums[j]} = {nums[i] + nums[j]}")
                if i == j:
                    print("es el mismo")
                    break
                if nums[i] + nums[j] == target:
                    return [i, j]

sol = Solution()
print(sol.twoSum([3,2,4], 6))