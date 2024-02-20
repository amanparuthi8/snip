"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45"""



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

