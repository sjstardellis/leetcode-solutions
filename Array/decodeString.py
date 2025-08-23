class Solution(object):
    def decodeString(self, s):
        stack = []
        # keep track of how many repeats
        current_num = 0
        current_str = ""


        for c in s:
            # if we hit a digit
            if c.isdigit():
                # handles multiple digits
                current_num = current_num * 10 + int(c)
            # if we hit an open bracket
            elif c == '[':
                # add the current string and the number onto the stack
                stack.append((current_str, current_num))
                # current_str our variables
                current_str = ''
                current_num = 0
            # if we hit a close bracket
            elif c == ']':
                # pop the previous string and number off the stack
                prev_str, num = stack.pop()
                # add to the current_str by taking the current_str and duplicating it num times, adding to the previous string
                current_str = prev_str + current_str * num
            else:
                # otherwise, add to the current string
                current_str += c

        return current_str