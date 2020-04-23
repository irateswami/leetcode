#!/usr/bin/env python3

import collections

class Solution:
    def isPalindrome(self, x: int) -> bool:

        y = list(str(x))
        z = list(str(x))
        z.reverse()

        if '-' in z:
            return False
        elif int("".join(y)) == int("".join(z)):
            return True 
        else:
            return False 

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-131))
print(s.isPalindrome(10))
