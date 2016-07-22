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
        _workweek_start = self._clean_weekday_param(workweek_start)[0]
        _workweek_end = self._clean_weekday_param(workweek_end)[0]

        _workday_calendar = set()

        for day in self.weekday_calendar():
            if day[1].weekday() in range(_workweek_start, _workweek_end + 1) and day[1].year == self.year:
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

        _workweek_start = self._clean_weekday_param(workweek_start)[0]
        _workweek_end = self._clean_weekday_param(workweek_end)[0]

        _month_calendar = set()

        if work:
            _cal = self.workday_calendar(_workweek_start, _workweek_end)

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

        _weekday = self._clean_weekday_param(weekday)
        _weekday_list = set()

        if month:
            _cal = self.month(month=month)

        else:
            _cal = self.weekday_calendar()

        for day in _cal:
            if day[1].weekday() in _weekday:
                _weekday_list.add(day)

        if ordinal:
            return sorted(list(_weekday_list), key=lambda x: x[1])[ordinal - 1]
        else:
            return sorted(list(_weekday_list), key=lambda x: x[1])

    @staticmethod
    def _clean_weekday_param(weekday_arg):
        """
        Takes the given weekday argument from the user and returns a set of integers for input.
        :param weekday_arg: (int) or (str) or (list) or (tuple) input argument from user
        :return: (set)
        """

        _weekday_lookup = {
            "Monday": 0,
            "Tuesday": 1,
            "Wednesday": 2,
            "Thursday": 3,
            "Friday": 4,
            "Saturday": 5,
            "Sunday": 6
        }

        if isinstance(weekday_arg, str):
            _cleaned_arg = {_weekday_lookup[weekday_arg.title()]}

        elif isinstance(weekday_arg, int) and weekday_arg in range(0, 7):
            _cleaned_arg = {weekday_arg}

        elif isinstance(weekday_arg, list) or isinstance(weekday_arg, tuple):
            _cleaned_arg = set()
            for w in weekday_arg:
                if isinstance(w, str):
                    w = _weekday_lookup[w.title()]
                elif isinstance(w, int) and w in range(0, 7):
                    w = w

                _cleaned_arg.add(w)

        return sorted(list(_cleaned_arg))
