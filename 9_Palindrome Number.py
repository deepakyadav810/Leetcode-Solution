class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        x=str(x)
        y=x[::-1]
        j=0
        c=0
        for i in range(len(x)):
            j=i
            if(x[i]==y[j]):
                c=c+1
        x=int(x)
        if(len(y)==c):
            if (-(2**31) < x < (2**31)-1):
                return True
            else:
                return False
        else:
            return False
