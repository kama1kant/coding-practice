from typing import List


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if len(stack) > 0 and s[i] == ')' and stack[-1][list(stack[-1].keys())[0]] == '(':
                stack.pop()
            elif s[i] == '(' or s[i] == ')':
                stack.append({i: s[i]})
                
        remove_id = []
        for i in stack:
            remove_id.append(list(i.keys())[0])
        
        print(stack)
        print(remove_id)
        
        ans = ''
        for i in range(len(s)):
            if i not in remove_id:
                ans += s[i]
            else:
                remove_id.remove(i)
        
        return ans
        
sol = Solution()
output = sol.minRemoveToMakeValid("())()(((")
print(output)

# New
# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         stack = []
#         for i, c in enumerate(s):
#             if c == '(' or c == ')':
#                 if c == ')' and len(stack) > 0 and s[stack[-1]] == '(':
#                     stack.pop()
#                 else:
#                     stack.append(i)
#         ans = ''
#         for i, c in enumerate(s):
#             if i not in stack:
#                 ans += c
#         return ans


# sol = Solution()
# print(sol.minRemoveToMakeValid('lee(t(c)o)de)'))
