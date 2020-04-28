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

        combos = {
                "IV":4,
                "IX":9,
                "XL":40,
                "XS":90,
                "CD":400,
                "CM":900
                }
       
        tupe2 = tuple(s[1::2])
        tupe1 = tuple(s[::2])

        #if len(s) is 3:


        for x in range(len(tupe2)):
            if len(s) is 3:
                return values[tupe1[x]] + values[tupe2[x]] + values[tupe1[x+1]e
            elif tupe1[x]+tupe2[x] in combos:
                total += combos[tupe1[x]+tupe2[x]]
            elif tupe2[x]+tupe1[x+1] in combos:
                total += combos[tupe2[x]+tupe1[x+1]]
            else:
                total += values[tupe1[x]] + values[tupe2[x]]

        return total

s1 = Solution()

#print(s1.romanToInt("III"))
#print(s1.romanToInt("IV"))
#print(s1.romanToInt("LVIII"))
#print(s1.romanToInt("IX"))
print(s1.romanToInt("XIV"))
print(s1.romanToInt("MMMDCCXXIV"))

