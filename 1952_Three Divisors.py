class Solution:
    def isThree(self, n: int) -> bool:
        count=0
        i=1
        while(i<=n):
            if(n%i==0) :
                count=count+1    
            i = i + 1
        if(count==3):
            return True
        else:
            return False
          
#uncomment to check with the testcases by changing value of n
"""          
n=111
obj=Solution
print(Solution().isThree(n))
"""
