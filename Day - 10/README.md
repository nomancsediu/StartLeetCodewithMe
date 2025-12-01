# Day 10: Valid Parentheses

## Problem Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Example 4:**
```
Input: s = "([)]"
Output: false
```

**Example 5:**
```
Input: s = "{[]}"
Output: true
```

## Solution Approach

This solution uses **Stack Data Structure**:

1. **Push Opening Brackets**: Add all opening brackets to stack
2. **Match Closing Brackets**: For each closing bracket, check if it matches the most recent opening bracket
3. **Validate Stack**: Ensure stack is empty at the end (all brackets matched)

### Algorithm Steps:
1. Initialize an empty stack (list)
2. Iterate through each character in the string:
   - If it's an opening bracket `(`, `[`, `{`: push to stack
   - If it's a closing bracket `)`, `]`, `}`:
     - Check if stack is empty (no matching opening bracket)
     - Pop from stack and verify it matches the closing bracket
3. Return true if stack is empty (all brackets matched)

## Code Implementation

```python
class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        a=[]
        n = len(s)
        for i in range(n):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                a.append(s[i])
            else:
                if not a:
                    return False
                top = a.pop()
                if s[i]==')' and top!='(':
                    return False
                if s[i]==']' and top!='[':
                    return False
                if s[i]=='}' and top!='{':
                    return False
                
        return len(a) == 0
```

## Complexity Analysis

- **Time Complexity**: O(n) - Single pass through the string
- **Space Complexity**: O(n) - Stack can hold up to n/2 opening brackets in worst case

## Alternative Approaches

### Using Dictionary for Mapping
```python
def isValid(self, s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack
```

## Key Points

1. **Stack LIFO**: Last In First Out property ensures correct bracket matching order
2. **Early Return**: Return false immediately when mismatch is found
3. **Empty Stack Check**: Prevent popping from empty stack
4. **Final Validation**: Stack must be empty for valid parentheses

## How to Run

1. Make sure you have Python installed
2. Create an instance of Solution and call isValid:
   ```python
   solution = Solution()
   result = solution.isValid("()[]{}")
   print(result)  # Output: True
   ```

## Test Cases

```python
# Test Case 1
s = "()"
# Expected: True

# Test Case 2
s = "()[]{}"
# Expected: True

# Test Case 3
s = "(]"
# Expected: False

# Test Case 4
s = "([)]"
# Expected: False

# Test Case 5
s = "{[]}"
# Expected: True
```

## LeetCode Link
[Valid Parentheses - LeetCode Problem #20](https://leetcode.com/problems/valid-parentheses/)

## Tags
- String
- Stack
- Parentheses

---
**Difficulty**: Easy  
**Day**: 10  
**Status**: ✅ Solved