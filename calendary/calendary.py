# -*- coding: utf-8 -*-
import calendar


class Calendary(object):
    """
    Class for common calendar operations.
    """

    def __init__(self, year):
        self.year = year
        self.year_calendar = (calendar.Calendar().yeardatescalendar(self.year, 12)[0])

    def weekday_calendar(self):
        """
        Append the weekday to each date for the calendar year.
        :return (list) of tuples ((str) weekday, datetime.date)
        """
        _weekday_calendar = set()

        for month in self.year_calendar:
            for week in month:
                for day in week:
                    if day.year == self.year:
                        _weekday_calendar.add((calendar.day_name[day.weekday()], day))

        return sorted(list(_weekday_calendar), key=lambda x: x[1])

    def workday_calendar(self, workweek_start=0, workweek_end=4):
        """
        Append the workday to each date for the calendar year.
        :param workweek_start: (int) index of the weekday starting with Monday (0)
        :param workweek_end: (int) index of the weekday starting with Monday (0)
        :return (list) of tuples ((str) weekday, datetime.date)
        """
        _workday_calendar = set()

        for day in self.weekday_calendar():
            if day[1].weekday() in range(workweek_start, workweek_end + 1) and day[1].year == self.year:
                _workday_calendar.add(day)

        return sorted(list(_workday_calendar), key=lambda x: x[1])

    def month(self, month, work=False, workweek_start=0, workweek_end=4):
        """
        Get all of the days in a given month
        :param month: (int) the number of the month to collect days
        :param work: (bool) limit the returned days to monday - friday
        :param workweek_start: (int) index of the weekday starting with Monday (0)
        :param workweek_end: (int) index of the weekday starting with Monday (0)
        :return (list) of tuples ((str) weekday, datetime.date)
        """
        _month_calendar = set()

        if work:
            _cal = self.workday_calendar(workweek_start, workweek_end)
        else:
            _cal = self.weekday_calendar()

        for day in _cal:
            if day[1].month == month:
                _month_calendar.add(day)

        return sorted(list(_month_calendar), key=lambda x: x[1])

    def weekday(self, weekday, month=None, ordinal=None):
        """
        Get a list of all days in a month given a weekday name
        :param weekday: (str) name of the weekday
        :param month: (int) number of the month
        :param ordinal: (int) number of day in month or year (third thursday of month or year)
        :return (list) of tuples ((str) weekday, datetime.date)
        """
        _weekday = weekday.title()
        _weekday_list = set()

        if month:
            _cal = self.month(month=month)

        else:
            _cal = self.weekday_calendar()

        for day in _cal:
            if calendar.day_name[day[1].weekday()] == _weekday:
                _weekday_list.add(day)

        if ordinal:
            return sorted(list(_weekday_list), key=lambda x: x[1])[ordinal - 1]
        else:
            return sorted(list(_weekday_list), key=lambda x: x[1])
