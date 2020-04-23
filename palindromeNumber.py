#!/usr/bin/env python3

import collections

class Solution:
    def isPalindrome(self, x: int) -> bool:

        y = list(str(x))

        if '-' in y:
            return False
        else:
             z = len(y)-1

             for x in range(0, int(len(y)/2)):
                 if y[x] is y[z]:
                     z -= 1
                 else:
                     return False

        return True

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-131))
print(s.isPalindrome(10))
