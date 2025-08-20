class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # helper gcd function (no import needed)
        def gcd(a, b):
            # taking both lengths, start the while loop while b isn't 0
            while b:
                # using Euclidean algorithm for computing the greatest common divisor
                # we will be left with the GCD once b is 0
                temp = a
                a = b
                b = temp % a
                # could also do a, b = b, a % b
                return a

        # common divisor check, if there is not a pattern then return empty string
        if str1 + str2 != str2 + str1:
            return ""
        # since there is a gcd, we must find the gcd between the two strings
        # slice str1[:a] (from beginning to a)
        res = str1[:gcd(len(str1), len(str2))]
        return res
