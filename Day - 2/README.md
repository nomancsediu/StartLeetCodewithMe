# Day 2: Three Sum

## Problem Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1:**
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
```

**Example 2:**
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

**Example 3:**
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

## Solution Approach

This solution uses **Two Pointers Technique** with sorting:

1. **Sort the Array**: Sort to enable two-pointer approach and handle duplicates
2. **Fix First Element**: Use outer loop to fix the first element
3. **Two Pointers for Remaining**: Use left and right pointers for the remaining two elements
4. **Skip Duplicates**: Avoid duplicate triplets by skipping same values

### Algorithm Steps:
1. Sort the nums array
2. For each element at index i (0 to n-3):
   - Skip duplicates for the first element
   - Set left = i+1, right = n-1
   - While left < right:
     - Calculate sum = nums[i] + nums[left] + nums[right]
     - If sum < 0: move left pointer right
     - If sum > 0: move right pointer left
     - If sum == 0: add triplet and skip duplicates

## Code Implementation

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        v = []

        for i in range(len(nums)-2):

            if i>0 and nums[i]==nums[i-1]:
                continue
            

            left = i+1
            right = len(nums)-1

            while left<right:
                total = nums[i]+nums[left]+nums[right]

                if total<0:
                    left+=1
                elif total>0:
                    right-=1
                else:
                    v.append([nums[i],nums[left],nums[right]])

                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    
                    left+=1
                    right-=1

        return v
```

## Complexity Analysis

- **Time Complexity**: O(n²) - Outer loop O(n) × Inner two pointers O(n)
- **Space Complexity**: O(1) - Only using constant extra space (excluding output array)

## Key Points

1. **Sorting**: Essential for two-pointer approach and duplicate handling
2. **Duplicate Skipping**: Critical to avoid repeated triplets
3. **Two Pointers**: Efficient way to find pairs that sum to target
4. **Early Termination**: Continue when first element is duplicate

## How to Run

1. Make sure you have Python installed
2. Import the required typing module:
   ```python
   from typing import List
   ```
3. Create an instance of Solution and call threeSum:
   ```python
   solution = Solution()
   result = solution.threeSum([-1,0,1,2,-1,-4])
   print(result)  # Output: [[-1,-1,2],[-1,0,1]]
   ```

## Test Cases

```python
# Test Case 1
nums = [-1,0,1,2,-1,-4]
# Expected: [[-1,-1,2],[-1,0,1]]

# Test Case 2
nums = [0,1,1]
# Expected: []

# Test Case 3
nums = [0,0,0]
# Expected: [[0,0,0]]
```

## LeetCode Link
[3Sum - LeetCode Problem #15](https://leetcode.com/problems/3sum/)

## Tags
- Array
- Two Pointers
- Sorting

---
**Difficulty**: Medium  
**Day**: 2  
**Status**: ✅ Solved