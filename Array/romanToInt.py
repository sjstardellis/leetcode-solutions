class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for i in range(len(s) - 1):
            if symbol[s[i]] < symbol[s[i + 1]]:
                sum -= symbol[s[i]]
            else:
                sum += symbol[s[i]]
        # every character except the last one is looking ahead
        # the last character has no character to look ahead from
        sum = sum + symbol[s[-1]]
        return sum