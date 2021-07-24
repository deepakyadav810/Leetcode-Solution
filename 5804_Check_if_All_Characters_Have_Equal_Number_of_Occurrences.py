class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        l=[]
        for i in range(len(s)):
            count=0
            for j in range(len(s)):
                if(s[i]==s[j]):
                    count=count+1
            l.append(count)
        check=True
        for i in l:
            if(l[0]!=i):
                check=False
                break
        return check
