# Day 11: Plus One

## Problem Description

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading zero, except the number 0 itself.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

**Example 2:**
```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

**Example 3:**
```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

## Solution Approach

This solution uses **Carry Propagation** technique:

1. **Start from Right**: Begin from the least significant digit (rightmost)
2. **Handle Carry**: If digit < 9, increment and return; otherwise set to 0 and continue
3. **All 9s Case**: If all digits are 9, prepend 1 to the array of zeros

### Algorithm Steps:
1. Start from the last digit (i = len(digits) - 1)
2. While i >= 0:
   - If digits[i] < 9: increment it and return the array
   - Otherwise: set digits[i] = 0 and move to previous digit
3. If loop completes (all digits were 9): return [1] + digits

## Code Implementation

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1

        while i>=0:
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
            i-=1
        return[1]+digits
```

## Complexity Analysis

- **Time Complexity**: O(n) - In worst case, we traverse all digits once
- **Space Complexity**: O(1) - Only constant extra space (excluding output array modification)

## Key Points

1. **Rightmost First**: Process digits from right to left (least to most significant)
2. **Early Return**: Return immediately when no carry is needed
3. **Carry Propagation**: Handle cascading carries for consecutive 9s
4. **Edge Case**: All 9s require adding a new digit at the front

## Alternative Approaches

### Convert to Integer (Not Recommended for Large Numbers)
```python
def plusOne(self, digits: List[int]) -> List[int]:
    num = int(''.join(map(str, digits)))
    return [int(d) for d in str(num + 1)]
```
- **Issue**: Integer overflow for very large numbers

## How to Run

1. Make sure you have Python installed
2. Import the required typing module:
   ```python
   from typing import List
   ```
3. Create an instance of Solution and call plusOne:
   ```python
   solution = Solution()
   result = solution.plusOne([1,2,3])
   print(result)  # Output: [1,2,4]
   ```

## Test Cases

```python
# Test Case 1
digits = [1,2,3]
# Expected: [1,2,4]

# Test Case 2
digits = [4,3,2,1]
# Expected: [4,3,2,2]

# Test Case 3
digits = [9]
# Expected: [1,0]

# Test Case 4
digits = [9,9,9]
# Expected: [1,0,0,0]
```

## LeetCode Link
[Plus One - LeetCode Problem #66](https://leetcode.com/problems/plus-one/)

## Tags
- Array
- Math
- Simulation

---
**Difficulty**: Easy  
**Day**: 11  
**Status**: ✅ Solved