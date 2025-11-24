
# Day 3: 4Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, return all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

* 0 <= a, b, c, d < n
* a, b, c, and d are **distinct**
* nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order. The solution set must not contain duplicate quadruplets.

---

## Examples

**Example 1:**

```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

**Example 2:**

```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

---

## Solution Approach

This solution uses a combination of **Sorting + Two Nested Loops + Two Pointer Technique**.

### Key Idea:

We reduce the 4Sum problem into multiple 2Sum problems by fixing two numbers and using two pointers for the remaining two.

### Strategy:

1. Sort the array to make duplicate handling easier.
2. Use two loops to fix the first two numbers (`i` and `j`).
3. Apply two pointers (`left` and `right`) to find the remaining two numbers.
4. Skip duplicates at every level to avoid repeated quadruplets.

---

## Algorithm Steps

1. Sort the array.
2. Loop `i` from 0 to n-4

   * Skip duplicates for `i`
3. Loop `j` from i+1 to n-3

   * Skip duplicates for `j`
4. Set `left = j+1` and `right = n-1`
5. While `left < right`:

   * Calculate total = nums[i] + nums[j] + nums[left] + nums[right]
   * If total < target → move `left` right
   * If total > target → move `right` left
   * If total == target → store quadruplet and skip duplicates

---

## Code Implementation

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        v = []

        for i in range(0, n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        v.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1

        return v
```

---

## Example Walkthrough

Input:

```
nums = [1, 0, -1, 0, -2, 2]
target = 0
```

After sorting:

```
[-2, -1, 0, 0, 1, 2]
```

Possible valid quadruplets found:

* [-2, -1, 1, 2]
* [-2, 0, 0, 2]
* [-1, 0, 0, 1]

---

## Complexity Analysis

* **Time Complexity:** O(n³)

  * Two loops + Two pointer traversal
* **Space Complexity:** O(1) (excluding output storage)

---

## How to Run

```python
from typing import List

solution = Solution()
result = solution.fourSum([1,0,-1,0,-2,2], 0)
print(result)
```

---

## Test Cases

```python
# Test Case 1
nums = [1,0,-1,0,-2,2]
target = 0
# Expected: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Test Case 2
nums = [2,2,2,2,2]
target = 8
# Expected: [[2,2,2,2]]
```

---

## LeetCode Link

[https://leetcode.com/problems/4sum/](https://leetcode.com/problems/4sum/)

---

## Tags

* Array
* Two Pointers
* Sorting
* Hashing

---

**Difficulty:** Medium
**Day:** 3  
**Status:** ✅ Solved
