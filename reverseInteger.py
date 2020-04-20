#!/usr/bin/env python3

class Solution:
    def reverse(self, x: int) -> int:

        newX = x
        isNegative = False

        if x < 0:
            newX = x*-1
            isNegative = True


        numArray = [str(num) for num in str(newX)]

        reversedArray = [] 

        for i in range(len(numArray)):
            reversedArray.insert(i, numArray.pop())

        reversedInt = int("".join(reversedArray)) 

        if(abs(reverseInt) > (2 ** 31 - 1)):
            return 0

        if isNegative == True:
            return reversedInt*-1
        else:
            return reversedInt


s1 = Solution()
print(s1.reverse(-678))
