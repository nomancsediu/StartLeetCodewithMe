# Day 4: Three Sum Closest

## Problem Description

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is **closest** to `target`. Return the sum of the three integers.

You may assume that each input would have **exactly one solution**.

---

## Examples

**Example 1:**

```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2 (-1 + 2 + 1 = 2).
```

**Example 2:**

```
Input: nums = [0,0,0], target = 1
Output: 0
```

---

## Solution Approach

This solution uses the **Two Pointer Technique** combined with sorting:

1. **Sort the Array** to allow two-pointer traversal.
2. **Iterate** through each number, fixing it as the first number of the triplet.
3. **Two Pointers**: Use `left` and `right` pointers for the remaining two numbers.
4. **Check Sum**:

   * If the sum equals the target, return immediately.
   * Update `closest` if the current sum is nearer to the target.
5. Move pointers based on comparison with the target to explore all possibilities efficiently.

---

## Algorithm Steps

1. Sort `nums`.
2. Initialize `closest = infinity`.
3. Loop `i` from 0 to n-3:

   * Set `left = i+1` and `right = n-1`.
   * While `left < right`:

     * Calculate `total = nums[i] + nums[left] + nums[right]`.
     * If `total == target` → return `target`.
     * If `abs(target - total) < abs(target - closest)` → update `closest = total`.
     * If `total < target` → move `left` right.
     * Else → move `right` left.
4. Return `closest` after traversing all triplets.

---

## Code Implementation

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')

        for i in range(0, n-2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == target:
                    return target

                if abs(target - closest) > abs(target - total):
                    closest = total

                if total < target:
                    left += 1
                else:
                    right -= 1

        return closest
```

---

## Complexity Analysis

* **Time Complexity:** O(n²) — sorting + nested two-pointer traversal
* **Space Complexity:** O(1) — only variables used, no extra data structures
---

## Test Cases

```python
# Test Case 1
nums = [-1,2,1,-4]
target = 1
# Expected: 2

# Test Case 2
nums = [0,0,0]
target = 1
# Expected: 0
```

---

## LeetCode Link

[Three Sum Closest - LeetCode #16](https://leetcode.com/problems/3sum-closest/)

---

## Tags

* Array
* Two Pointers
* Sorting

---

**Difficulty:** Medium
**Day:** 4
**Status:** ✅ Solved
