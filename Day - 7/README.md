# Day 7 - Merge Two Sorted Lists

## Problem Description
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## Examples

### Example 1:
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Example 2:
```
Input: list1 = [], list2 = []
Output: []
```

### Example 3:
```
Input: list1 = [], list2 = [0]
Output: [0]
```

## Constraints
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

## Solution Approach
1. Create a dummy node to simplify the merging process
2. Use two pointers to traverse both linked lists
3. Compare values and attach the smaller node to the result
4. Handle remaining nodes from either list
5. Return the merged list starting from dummy.next

## Time & Space Complexity
- **Time Complexity:** O(m + n) where m and n are lengths of the two lists
- **Space Complexity:** O(m + n) for creating new nodes

## LeetCode Link
[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)