class Solution:
    def isValid(self, s: str) -> bool:
        # key-value pairs of our brackets, stack to keep track of open/closed brackets
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            # if the character is in the values mapping (meaning it's an open parenthesis)
            if char in mapping.values():
                # add to the stack
                stack.append(char)
            # if the character is a key (meaning it's a closed parenthesis)
            elif char in mapping:
                # if the stack is empty or the character doesn't match the corresponding pair at the top of the stack
                if not stack or mapping[char] != stack.pop():
                    # return false
                    return False
        # return true if the stack is empty
        return not stack