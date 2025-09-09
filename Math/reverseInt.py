class Solution:
    def reverse(self, x: int) -> int:
        # returns true if x is less than 0
        isNegative = x < 0
        # turns x into positive
        x = abs(x)

        # reverse digits
        # sequence[start:end:step], basically go through entire string backwards
        digits = str(x)[::-1]
        x = int(digits)

        if isNegative:
            x = -x
        # our limits for our integer
        if x < -2**31 or x > 2**31 - 1:
            return 0

        return x
