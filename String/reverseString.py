class Solution:
    def reverseWords(self, s: str) -> str:
        # our temporary string, just trying to remove spaces
        delimiter = ""
        for ch in s:
            # if we hit a space
            if ch == " ":
                # check to see if delimiter is empty or if the last character is not "#"
                if not delimiter or delimiter[-1] != "#":
                    # adds "#" to the end of the temp string
                    delimiter += "#"
            else:
                # if not a space, just add the character
                delimiter += ch
        # now we have our temporary string built, we need to build the solution
        # result
        reverse = ""
        # construct word
        word = ""
        # go through the characters of the delimiter
        for ch in delimiter:
            # if it is not a delimiter character, add to the word
            if ch != "#":
                word += ch
            # if it is a delimiter
            else:
                # if the word is not empty
                if word:
                    # if reverse is not empty
                    if reverse:
                        # then add a space between word and reverse and combine the wo
                        reverse = word + " " + reverse
                    else:
                        # otherwise, if reverse is empty, that means we are at the first word
                        reverse = word
                # reset word
                word = ""
        # for the last word, if word is not empty
        if word:
            # if reverse is not empty
            if reverse:
                # then add a space between word and reverse and combine the wo
                reverse = word + " " + reverse
            else:
                # otherwise, if reverse is empty, that means we are at the first word
                reverse = word

        return reverse
