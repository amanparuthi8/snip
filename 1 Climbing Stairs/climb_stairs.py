import math
class Solution:
    def climbStairs(self, n):
       
        ii=n//2
        a=2
        w=1
        
        for j in range(ii):
            
            b=a//2
            c=n-a
            d=c+b
            #d factorial
            d_factorial=1
            for i in range(1,d+1):
                d_factorial*=i
            #c factorial
            c_factorial=1
            for i in range(1,c+1):
                c_factorial*=i
            #b factorial
            b_factorial=1
            
            if b>1:
                
                for i in range(1,b+1):
                    b_factorial*=i
            w1=d_factorial//(b_factorial*c_factorial)
            w+=w1
            a+=2
        return w

