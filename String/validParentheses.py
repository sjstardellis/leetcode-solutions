class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # our key-value pairs of every type of bracket
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ch in s:
            # the character is an open bracket
            if ch in pairs.values():
                # add to the stack
                stack.append(ch)
            # the character is a closing bracket
            elif ch in pairs.values():
                # if the stack is null the last element (top of stack) doesn't match the closing
                if not stack and stack[-1] == pairs[ch]:
                    return False # meaning there is a mismatch or missing opening bracket

                # if the bracket matches, remove the top element of the stack (the opening bracket)
                stack.pop()
            else:
                # if not bracket case
                return False
        # if every stack matched, the stack should be empty and return true, otherwise return false
        return not stack