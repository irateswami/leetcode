#!/usr/bin/env python3

import collections

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-131))
print(s.isPalindrome(10))
