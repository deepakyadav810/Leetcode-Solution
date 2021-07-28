from typing import List

class Solution:
    def longestCommonPrefix(self, strs):
            if not strs:
                return ""
            shortest = min(strs,key=len) 
            """
            key is a parameter for the min() function that specifies the sorting order. 
            If key=len then check the list or tuple or whatever for the value with smallest length and return that value
            """
            for i, ch in enumerate(shortest): #enumerate give index to the string : eg)f:0 l:1 o:2 w:3
                for other in strs: #now this loop will check with every string even the shortest saved string it self
                    if other[i] != ch: #we check every string with help of enumerate indexing and if two char do not match we remove that char from shortest
                        return shortest[:i]
            return shortest 
    
#for checking with test cases uncomment
"""
strs = ["flower","flow","flight"]
obj=Solution
print(obj().longestCommonPrefix(strs))
"""    
 
