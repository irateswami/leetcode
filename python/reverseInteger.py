#!/usr/bin/env python3

class Solution:
    def reverse(self, x: int) -> int:

        y = str(abs(x))[::-1]
        
        if int(y) > 2147483647:
            return 0
        elif x < 0:
            return int(y)*-1
        else:
            return int(y)

s1 = Solution()
print(s1.reverse(-678))

print(s1.reverse(1563847412))
