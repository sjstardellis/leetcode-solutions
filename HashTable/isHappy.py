class Solution:
    def isHappy(self, n: int) -> bool:
        # base cases
        if(n==1 or n==7):
            return True
        # cycle
        elif(n<10):
            return False
        else:
            # running sum
            sum = 0
            while(n>0):
                # get the last digit
                temp = n % 10
                # square the last digit and add it to the sum
                sum += temp*temp
                # remove last digit
                n= n//10
            # call the function again with new sum
            return self.isHappy(sum)