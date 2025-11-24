# Day 1: 2Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Solution Approach

This solution uses a **Two Pointer Technique** with sorting:

1. **Store Original Array**: Keep a copy of the original array to track original indices
2. **Sort the Array**: Sort the nums array to enable two-pointer approach
3. **Two Pointers**: Use left and right pointers to find the target sum
4. **Find Original Indices**: Map the found values back to their original positions

### Algorithm Steps:
1. Create a copy of the original array
2. Sort the nums array
3. Initialize left pointer at start (0) and right pointer at end (n-1)
4. While left < right:
   - If sum equals target, break
   - If sum < target, move left pointer right
   - If sum > target, move right pointer left
5. Find original indices of the two numbers in the unsorted array

## Code Implementation

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1

        a = []

        for num in nums:
            a.append(num)

        nums.sort()

        v = []

        while left<right:
            summ = nums[left]+nums[right]
            if summ == target:
                break
            elif summ < target:
                left+=1
            else:
                right-=1
        
        for i in range(n):
            if nums[left] == a[i]:
                v.append(i)
            elif nums[right] == a[i]:
                v.append(i)

        return v
```

## Complexity Analysis

- **Time Complexity**: O(n log n) - Due to sorting the array
- **Space Complexity**: O(n) - For storing the copy of original array

## Alternative Approaches

### Hash Map Approach (More Efficient)
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

## How to Run

1. Make sure you have Python installed
2. Import the required typing module:
   ```python
   from typing import List
   ```
3. Create an instance of Solution and call twoSum:
   ```python
   solution = Solution()
   result = solution.twoSum([2, 7, 11, 15], 9)
   print(result)  # Output: [0, 1]
   ```

## Test Cases

```python
# Test Case 1
nums = [2, 7, 11, 15]
target = 9
# Expected: [0, 1]

# Test Case 2
nums = [3, 2, 4]
target = 6
# Expected: [1, 2]

# Test Case 3
nums = [3, 3]
target = 6
# Expected: [0, 1]
```

## LeetCode Link
[Two Sum - LeetCode Problem #1](https://leetcode.com/problems/two-sum/)

## Tags
- Array
- Hash Table
- Two Pointers
- Sorting

---
**Difficulty**: Easy  
**Day**: 1  
**Status**: ✅ Solved
