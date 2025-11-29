# Day 8: Merge Sorted Array

## Problem Description

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to 0 and should be ignored. `nums2` has a length of `n`.

**Example 1:**
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

**Example 2:**
```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
```

**Example 3:**
```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
```

## Solution Approach

This solution uses **Three Pointers Technique** working backwards:

1. **Start from End**: Begin merging from the end of nums1 to avoid overwriting elements
2. **Compare Elements**: Compare elements from both arrays and place the larger one at the end
3. **Handle Remaining**: Continue until all elements from nums2 are processed

### Algorithm Steps:
1. Initialize three pointers: i (last element of nums1), j (last element of nums2), k (last position in merged array)
2. While there are elements in nums2 to process:
   - If nums1[i] >= nums2[j], place nums1[i] at position k and decrement i
   - Otherwise, place nums2[j] at position k and decrement j
   - Decrement k after each placement
3. Continue until all elements from nums2 are merged

## Code Implementation

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
```

## Complexity Analysis

- **Time Complexity**: O(m + n) - We process each element exactly once
- **Space Complexity**: O(1) - Only using constant extra space, in-place modification

## Key Points

1. **Backwards Merging**: Prevents overwriting unprocessed elements in nums1
2. **In-place Modification**: No extra space needed for the result
3. **Handle Edge Cases**: Works when one array is empty or when all elements from one array are larger
4. **Optimal Approach**: Single pass through both arrays

## How to Run

1. Make sure you have Python installed
2. Import the required typing module:
   ```python
   from typing import List
   ```
3. Create an instance of Solution and call merge:
   ```python
   solution = Solution()
   nums1 = [1,2,3,0,0,0]
   nums2 = [2,5,6]
   solution.merge(nums1, 3, nums2, 3)
   print(nums1)  # Output: [1,2,2,3,5,6]
   ```

## Test Cases

```python
# Test Case 1
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m, n = 3, 3
# Expected: [1,2,2,3,5,6]

# Test Case 2
nums1 = [1]
nums2 = []
m, n = 1, 0
# Expected: [1]

# Test Case 3
nums1 = [0]
nums2 = [1]
m, n = 0, 1
# Expected: [1]
```

## LeetCode Link
[Merge Sorted Array - LeetCode Problem #88](https://leetcode.com/problems/merge-sorted-array/)

## Tags
- Array
- Two Pointers
- Sorting

---
**Difficulty**: Easy  
**Day**: 8  
**Status**: ✅ Solved