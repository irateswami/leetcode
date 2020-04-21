#!/usr/bin/env python3

class Solution:
    def reverse(self, x: int) -> int:

        y = list(str(abs(x)))

        y.reverse()

        num = int("".join(y))  
        
        if num > 2147483647:
            return 0
        elif x < 0:
            return num*-1
        else:
            return num

s1 = Solution()
print(s1.reverse(-678))

print(s1.reverse(1563847412))
