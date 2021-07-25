class Solution:
    def reverse(self, x: int) -> int:
        res=1
        if(x<0):
            res=-1
        res=res*int(str(abs(x))[::-1])
        if(-(2**31) < res < (2**31-1)):
            return res
        else:
            return 0
            
