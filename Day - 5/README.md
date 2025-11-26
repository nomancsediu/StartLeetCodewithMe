# Day 5: Contains Duplicate

## Problem Description

You are given an integer array `nums`.
Your task is to determine whether any value appears at least twice in the array.

* Return `true` if any duplicate exists.
* Return `false` if all elements are unique.

---

## Examples

### Example 1

Input:

```
nums = [1, 2, 3, 1]
```

Output:

```
true
```

Explanation: The number `1` appears more than once.

### Example 2

Input:

```
nums = [1, 2, 3, 4]
```

Output:

```
false
```

Explanation: All elements are distinct.

---

## Solution Approach

This solution uses a **Hash Set** to track previously seen numbers.

### Key Idea:

* A set does not allow duplicate values.
* While iterating through the array, if a number already exists in the set, a duplicate has been found.

---

## Algorithm Steps

1. Initialize an empty set `hash_set`.
2. Loop through each element in `nums`.
3. If the element already exists in the set:

   * Return `true`.
4. Otherwise, add the element to the set.
5. If the loop finishes without finding duplicates:

   * Return `false`.

---

## Code Implementation

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for i in nums:
            if i in hash_set:
                return True
            else:
                hash_set.add(i)
        return False
```

---

## Complexity Analysis

* **Time Complexity:** O(n)
  Each element is checked once.

* **Space Complexity:** O(n)
  In the worst case, all elements are stored in the set.

---

## Test Cases

### Test Case 1

```
nums = [1, 2, 3, 1]
Expected Output: true
```

### Test Case 2

```
nums = [1, 2, 3, 4]
Expected Output: false
```

---

## LeetCode Link

Contains Duplicate - LeetCode #217

---

## Tags

* Array
* Hash Table
* Set

**Difficulty:** Easy
**Day:** 5
**Status:** ✅ Solved
