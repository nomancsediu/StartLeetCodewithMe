# Day 9: Palindrome Number

## Problem Description

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

An integer is a palindrome when it reads the same backward as forward.

**Example 1:**
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

**Example 2:**
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## Solution Approach

This solution uses **Number Reversal** technique:

1. **Handle Negative Numbers**: Return false immediately for negative numbers
2. **Reverse the Number**: Build the reversed number digit by digit
3. **Compare**: Check if the reversed number equals the original

### Algorithm Steps:
1. If x < 0, return false (negative numbers can't be palindromes)
2. Initialize rev = 0 and num = x
3. While num > 0:
   - Extract last digit: num % 10
   - Add to reversed number: rev = rev * 10 + digit
   - Remove last digit from num: num //= 10
4. Return true if rev equals original x

## Code Implementation

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = 0
        num = x
        while num:
            rev = rev * 10 + num % 10
            num //= 10 
        
        return rev == x
```

## Complexity Analysis

- **Time Complexity**: O(log n) - Where n is the input number (number of digits)
- **Space Complexity**: O(1) - Only using constant extra space

## Alternative Approaches

### String Conversion Approach
```python
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]
```
- **Time Complexity**: O(log n)
- **Space Complexity**: O(log n) - For string conversion

### Half Reversal Approach (More Efficient)
```python
def isPalindrome(self, x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    
    return x == rev or x == rev // 10
```

## Key Points

1. **Negative Numbers**: Always false for palindrome check
2. **Number Reversal**: Extract digits using modulo and division operations
3. **No String Conversion**: Pure mathematical approach without extra space
4. **Edge Cases**: Handle 0 and single-digit numbers correctly

## How to Run

1. Make sure you have Python installed
2. Create an instance of Solution and call isPalindrome:
   ```python
   solution = Solution()
   result = solution.isPalindrome(121)
   print(result)  # Output: True
   ```

## Test Cases

```python
# Test Case 1
x = 121
# Expected: True

# Test Case 2
x = -121
# Expected: False

# Test Case 3
x = 10
# Expected: False

# Test Case 4
x = 0
# Expected: True
```

## LeetCode Link
[Palindrome Number - LeetCode Problem #9](https://leetcode.com/problems/palindrome-number/)

## Tags
- Math
- Palindrome

---
**Difficulty**: Easy  
**Day**: 9  
**Status**: ✅ Solved