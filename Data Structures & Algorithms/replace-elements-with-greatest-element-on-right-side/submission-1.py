"""
# Questions
- Empty array? empty
- Single element? [-1]
- In place replacement? Yes
- Negatives? Yes

# Input
- arr: int[]


# Output
- arr: int[]

# Approach
## 1
- Time: O(n ^ 2) . n -> lenght of numbers
- Space: O(1)
1. Iterate over array
2. For each element look for greatest at the right

## 2
- Time: O(n)
- Space: O(n)
1. First past over the array from right to left
2. Keep a new array to store max 
3. Iterate over the array and replace based on the new one

## 3
- Time: O(n)
- Space: O(1)
1. Two pointers
2. Iterate from right - left
3. Keep track of max
4. Replace left with right who keeps the max 



"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr

        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(arr[i], rightMax)
            arr[i] = rightMax

            rightMax = newMax
            
        return arr
        