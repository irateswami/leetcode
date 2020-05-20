#!/usr/bin/env python3

class Solution:

    def romanToInt(self, s: str) -> int:

        total = 0

        values = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        res = 0 
        prev = ""

        for item in s:
            res+=values.get(item)

            if (prev+item) in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                res -= 2*values.get(prev)

            prev = item

        return res



s1 = Solution()

print(s1.romanToInt("III"))
print(s1.romanToInt("IV"))
print(s1.romanToInt("LVIII"))
print(s1.romanToInt("IX"))
print(s1.romanToInt("XIV"))
print(s1.romanToInt("MMMDCCXXIV"))

