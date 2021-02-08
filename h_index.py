# Brute Force - H index is the index where the value of citation crosses len(arr) - idx 
# Time - O(N)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        n = len(citations)
        for idx, c in enumerate(citations):
            
            if c >= n - idx:
                
                return n - idx
        return 0


# Optimized solution
# Since array is sorted, we can do binary search
# Time - O(log N)
# Space - O(1)

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        if not citations or len(citations) == 0:
            return 0

        low = 0
        high = len(citations) - 1
        n = len(citations)

        while low <= high:

            midd = low + (high - low) // 2

            if citations[midd] == n - midd:
                return n - midd
            
            elif citations[midd] < n - midd:
                low = midd + 1

            else:
                high = midd - 1

        return n - low # edge case when we have only one citation

