class Solution:
    def romanToInt(self, s: str) -> int:
        dict={'I' :1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        for i in range(0,len(s)): 
            if(i<(len(s)-1)): #this condition is to rectify string index out of range for the next condition   
                if(dict[s[i]]<dict[s[i+1]]): #it checks if next element is greater than itself : if yes will continue
                    continue
                elif(dict[s[i-1]]<dict[s[i]] and i>0): #it checks previous element is small : if yes then subtract previous element
                    num=num+((dict[s[i]])-(dict[s[i-1]]))
                else:
                    num=num+dict[s[i]]
            elif(i==(len(s)-1)): #this condition is to rectify string index out of range for last element as if we had executed in above condition it would show error  
                if(dict[s[i-1]]<dict[s[i]]): #it checks if previous element is less than itself : if yes then subtract previous element 
                    num=num+((dict[s[i]])-(dict[s[i-1]]))
                else:
                    num=num+dict[s[i]]
            else:
                num=num+dict[s[i]]
        return num
