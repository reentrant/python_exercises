"""
Created on 08/01/2018

@author: jruiz
"""
# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.


def is_leap_year(year: int):
    """ From wikipedia:
    if (year is not divisible by 4) then (it is a common year)
    else if (year is not divisible by 100) then (it is a leap year)
    else if (year is not divisible by 400) then (it is a common year)
    else (it is a leap year)
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def get_max_days_in_a_month(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) and month == 2:
        return 29
    else:
        return days_in_month[month - 1]


def get_next_day_date(year, month, day):
    """Updated version..."""
    if day < get_max_days_in_a_month(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def is_date_before(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        


def calculate_days_between_dates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not is_date_before(year2, month2, day2, year1, month1, day1)
    days = 0
    while is_date_before(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = get_next_day_date(year1, month1, day1)
        days += 1
    # print(f"Year: {year1} {days}")
    return days


def using_assertions():
    assert get_next_day_date(2016, 2, 28) == (2016, 2, 29)
    assert get_next_day_date(2016, 2, 29) == (2016, 3, 1)
    assert get_next_day_date(2017, 12, 31) == (2018, 1, 1)
    assert get_next_day_date(2013, 1, 1) == (2013, 1, 2)
    assert get_next_day_date(2013, 4, 30) == (2013, 5, 1)
    assert get_next_day_date(2012, 12, 31) == (2013, 1, 1)

    assert calculate_days_between_dates(2018, 1, 6, 2018, 1, 6) == 0
    assert calculate_days_between_dates(2018, 1, 1, 2018, 1, 2) == 1


def unit_test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = calculate_days_between_dates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


def main():
    pass


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"Date <year: {self.year}, month: {self.month}, day:{self.day}>"


class DaysCalculator:
    def __init__(self, date1, date2):
        self.initial_date = date1
        self.later_date = date2

    def calculate_days_between_dates(self):
        """Returns the number of days between self.initial_date and self.later_date.
            Assumes inputs are valid dates in Gregorian calendar."""
        # program defensively! Add an assertion if the input is not valid!
        assert not self.is_date_before(self.later_date, self.initial_date)
        days = 0
        while self.is_date_before(self.initial_date, self.later_date):
            self.initial_date.year, self.initial_date.month, self.initial_date.day = self.get_next_day_date(
                self.initial_date)
            days += 1
        return days

    @staticmethod
    def is_date_before(first_date, later_date):
        if first_date.year < later_date.year:
            return True
        if first_date.year == later_date.year:
            if first_date.month < later_date.month:
                return True
            if first_date.month == later_date.month:
                return first_date.day < later_date.day
        return False

    @staticmethod
    def get_next_day_date(date):
        """Updated version..."""
        if date.day < get_max_days_in_a_month(date.year, date.month):
            return date.year, date.month, date.day + 1
        else:
            if date.month == 12:
                return date.year + 1, 1, 1
            else:
                return date.year, date.month + 1, 1


if __name__ == '__main__':
    main()
    today = Date(2022, 7, 17)
    tomorrow = Date(2022, 7, 18)
    subtractor = DaysCalculator(today, tomorrow)
    print(subtractor.calculate_days_between_dates())
