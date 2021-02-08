# Brute Force - Explore all paths in both the arrays
# Time - O( M * N)

# Since arrays are sorted, use 2 pointers
# Time: O(m + n)
# Space: O(1)

def OptimalUtilization(self, forwardArray, returnArray, maxDist):
   
         
    m, n = len(forwardArray), len(returnArray)
    p1 = 0
    p2 = n - 1
    
    res = 0
    result = []
    
    while p1 < m and p2 < n:

        if forwardArray[p1][1] + returnArray[p2][1] > maxDist:
            p2 -= 1
        
        else:
            if forwardArray[p1][1] + returnArray[p2][1] > res:
                res = forwardArray[p1][1] + returnArray[p2][1]
                result = [[forwardArray[p1][0], returnArray[p2][0]]]
            
            elif forwardArray[p1][1] + returnArray[p2][1] == res:
                result.append([forwardArray[p1][0], returnArray[p2][0]])
            p1 += 1
    
    return result