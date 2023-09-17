from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        s_arr = []
        dict = {}
        final = []
        
        for str in strs:
            str = list(str)
            str.sort()
            if str not in s_arr:
                s_arr.append(str)
            print(s_arr)
            
        for i in range(len(strs)):
            str = list(strs[i])
            str.sort()
            print(strs[i])
            for j in range(len(s_arr)):
                if str == s_arr[j]:
                    dict[strs[i]] = j 
            print(dict)
        
        for i in range(len(s_arr)):
            final.append([])
            print(final)
            
        for str in strs:
            final[dict[str]].append(str)
        
        return final
            
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))