#!/usr/bin/env python3

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestWord = min(strs, key = len)
        shortestWordLen = len(shortestWord)
        
        for i in range(1, shortestWordLen):
            prefix = shortestWord[:i]

            for j in strs:

                if prefix not in j:
                    if i is 1:
                        return ""
                    else:
                        return prefix[:i-1]
                else:
                    continue

s = Solution()
strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]

print(s.longestCommonPrefix(strs1))
print(s.longestCommonPrefix(strs2))
