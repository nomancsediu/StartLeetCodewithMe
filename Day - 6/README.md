# Day 6: Contains Duplicate II

## Problem Description

Given an integer array `nums` and an integer `k`, determine if there are **two distinct indices** `i` and `j` in the array such that:

1. `nums[i] == nums[j]`
2. `abs(i - j) <= k`

Return `True` if such a pair exists, otherwise return `False`.

---

## Examples

**Example 1:**

```python
Input: nums = [1,2,3,1], k = 3
Output: True
# Explanation: nums[0] == nums[3] and |0-3| <= 3
```

**Example 2:**

```python
Input: nums = [1,0,1,1], k = 1
Output: True
# Explanation: nums[2] == nums[3] and |2-3| <= 1
```

**Example 3:**

```python
Input: nums = [1,2,3,1,2,3], k = 2
Output: False
# Explanation: No duplicates are within 2 indices of each other
```

---

## Solution Approach

This solution uses a **Hash Map** to track the **last seen index** of each number:

1. Create an empty dictionary `last_seen_dict`.
2. Traverse the array using an index `i`.
3. For each number `num`:

   * If `num` exists in the dictionary and the distance from the current index to the last seen index ≤ `k`, return `True`.
   * Otherwise, update the dictionary with the current index for that number.
4. Return `False` if no nearby duplicate is found.

> Key idea: **Store the last index of each number** to check if the next occurrence is within `k`.

---

## Algorithm Steps

1. Initialize an empty dictionary: `last_seen_dict = {}`.
2. Loop over `nums` with index `i`:

   * Let `num = nums[i]`.
   * If `num` exists in `last_seen_dict`:

     * Check if `i - last_seen_dict[num] <= k`.
     * If yes → return `True`.
   * Update `last_seen_dict[num] = i`.
3. Return `False` at the end.

---

## Code Implementation

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        last_seen_dict = {}

        for index, key_value in enumerate(nums):
            if key_value in last_seen_dict and (index - last_seen_dict[key_value]) <= k:
                return True
            last_seen_dict[key_value] = index

        return False
```

---

## Complexity Analysis

* **Time Complexity:** O(n) — single pass through the array
* **Space Complexity:** O(n) — for the dictionary storing last seen indices

---

## Test Cases

```python
# Test Case 1
nums = [1,2,3,1]
k = 3
# Expected: True

# Test Case 2
nums = [1,0,1,1]
k = 1
# Expected: True

# Test Case 3
nums = [1,2,3,1,2,3]
k = 2
# Expected: False
```

---

## LeetCode Link

[Contains Duplicate II - LeetCode #219](https://leetcode.com/problems/contains-duplicate-ii/)

---

## Tags

* Array
* Hash Map
* Sliding Window (alternative approach)

---

**Difficulty:** Easy/Medium
**Day:** 6
**Status:** ✅ Solved
