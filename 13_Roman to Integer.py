class Solution:
    def romanToInt(self, s: str) -> int:
        dict={'I' :1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        for i in range(0,len(s)):
            if(i<(len(s)-1)):
                if(dict[s[i]]<dict[s[i+1]]):
                    continue
                elif(dict[s[i-1]]<dict[s[i]] and i>0):
                    num=num+((dict[s[i]])-(dict[s[i-1]]))
                else:
                    num=num+dict[s[i]]
            elif(i==(len(s)-1)):
                if(dict[s[i-1]]<dict[s[i]]):
                    num=num+((dict[s[i]])-(dict[s[i-1]]))
                else:
                    num=num+dict[s[i]]
            else:
                num=num+dict[s[i]]
        return num
