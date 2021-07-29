#This question can be solved by stack data structure
"""
Let's take a simple example : let the string be ([])
So logic we'll use is, we will create a list name 'stack' in that whenever
opening character comes (eg.'(','[','{') we will append. Also a dictonary will be created 
in which closing char will be the key and opening char will be its values.Now we will append 
those char to stack which are value and pop when dictionary key == value. So the first
char is '(' so we will append it to stack and go to next char which is '[' so now this is appended 
in stack. Next char comes ']' now we will use this char as key to get value of it and compare
with the poped value of stack if same we'll continue or return false. Like this at last if we get 
an empty stack then we return true.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        dic={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if char in dic.values():
                stack.append(char)
            elif char in dic.keys():
                if(stack == [] or dic[char]!=stack.pop()):
                    return False
            else:
                return False       
        return stack==[]
#to check any test cases uncomment and change value of s
"""
s = "([])"
obj=Solution
print(Solution().isValid(s))
"""
