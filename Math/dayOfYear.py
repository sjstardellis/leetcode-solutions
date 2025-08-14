class Solution:
    def dayOfYear(self, date: str) -> int:
        # slice out the string
        year = int(date[:4])
        input_month = int(date[5:7])
        day = int(date[8:])

        # set February days to 28, check if a leap year
        feb_days = 28
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            feb_days = 29

        # our dictionary to store our months and corresponding days
        month_days = {
            1: 31,
            2: feb_days,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        # sum all the days before the inputted month
        total_days_before = sum(
            # days at the beginning is the filter for the tuple
            # .month, days in month_days.items() returns each key–value pair from the dictionary
            # filter condition: if int(month) < int(input_month)
            days for month, days in month_days.items() if int(month) < int(input_month)
        )

        return total_days_before + day
