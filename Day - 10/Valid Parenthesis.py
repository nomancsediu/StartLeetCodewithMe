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
        