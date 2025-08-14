class Solution:
    def dayOfYear(self, date: str) -> int:
        # slice the numbers out
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        # days per month (Feb = 28)
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # leap year check
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            # set February to 29 if true
            month_days[1] = 29

        # sum days of all previous months + current day
        return sum(month_days[:month-1]) + day
