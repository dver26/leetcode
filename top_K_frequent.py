from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ns = []
        keys = []
        values = []
        sol = []
        
        for num in nums:
            if num not in ns: ns.append(num)
            print(ns)
        
        for n in ns:
            cnt = 0
            for num in nums:
                if n == num: cnt += 1
            values.append(cnt)
            keys.append(n)
            print(keys, values)

        for i in range(k):
            j = values.index(max(values))
            sol.append(keys[j])
            keys.pop(j)
            values.pop(j)

        print(sol)
                
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))