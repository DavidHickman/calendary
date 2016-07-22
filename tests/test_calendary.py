#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_calendary
----------------------------------

Tests for `calendary` module.
"""
import datetime

from calendary import Calendary


class TestCalendary(object):
    def test_calendary_weekday_calendar_is_list(self):
        cal = Calendary(2016)
        assert isinstance(cal.weekday_calendar(), list)

    def test_calendary_workday_calendar_is_list(self):
        cal = Calendary(2016)
        assert isinstance(cal.weekday_calendar(), list)

    def test_calendary_weekday_calendar_has_weekends_by_list(self):
        cal = Calendary(2016)
        weekends = [day for day in cal.weekday_calendar() if day[1].weekday() in [5, 6]]
        assert len(weekends) > 0

    def test_calendary_workday_calendar_has_no_weekends_by_list(self):
        cal = Calendary(2016)
        weekends = [day for day in cal.workday_calendar() if day[1].weekday() in [5, 6]]
        assert len(weekends) == 0

    def test_calendary_weekday_calendar_has_weekends_by_name(self):
        cal = Calendary(2016)
        weekends = [day for day in cal.weekday_calendar() if day[0] in ['Saturday', 'Sunday']]
        assert len(weekends) > 0

    def test_calendary_workday_calendar_has_no_weekends_by_name(self):
        cal = Calendary(2016)
        weekends = [day for day in cal.workday_calendar() if day[0] in ['Saturday', 'Sunday']]
        assert len(weekends) == 0

    def test_calendary_weekday_calendar_for_duplicates(self):
        cal = Calendary(2016)
        assert len(cal.weekday_calendar()) == len(set(cal.weekday_calendar()))

    def test_calendary_workday_calendar_for_duplicates(self):
        cal = Calendary(2016)
        assert len(cal.workday_calendar()) == len(set(cal.workday_calendar()))

    def test_calendary_weekday_month_only_returns_given_month(self):
        cal = Calendary(2016).month(7)
        days_in_july = [day for day in cal if day[1].month == 7]
        assert len(days_in_july) == 31

    def test_calendary_workday_month_only_returns_given_month(self):
        cal = Calendary(2016).month(7, work=True)
        days_in_july = [day for day in cal if day[1].month == 7]
        assert len(days_in_july) == 21

    def test_calendary_weekday_only_returns_given_day(self):
        cal = Calendary(2016).weekday('Thursday')
        not_thursday = [day for day in cal if day[1].weekday() != 3]
        assert len(cal) > 0
        assert len(not_thursday) == 0

    def test_calendary_weekday_returns_ordinal(self):
        third_tuesday_in_july = Calendary(2016).weekday('Tuesday', month=7, ordinal=3)
        assert third_tuesday_in_july == ('Tuesday', datetime.date(month=7, day=19, year=2016))

    def test_calendary_weekday_returns_right_day_for_year(self):
        first_monday_in_nineteen_fortyseven = Calendary(1947).weekday('Monday', ordinal=1)
        assert first_monday_in_nineteen_fortyseven == ('Monday', datetime.date(month=1, day=6, year=1947))

    def test_clean_weekday_param_string(self):
        string_weekday = Calendary._clean_weekday_param("Monday")
        assert isinstance(string_weekday, list)
        assert isinstance(string_weekday[0], int)

    def test_clean_weekday_param_list(self):
        string_weekday = Calendary._clean_weekday_param(["Monday", 3])
        assert isinstance(string_weekday, list)
        assert isinstance(string_weekday[0], int)

    def test_clean_weekday_param_tuple(self):
        string_weekday = Calendary._clean_weekday_param(("Monday", 3))
        assert isinstance(string_weekday, list)
        assert isinstance(string_weekday[0], int)

    def test_weekday_with_multiple_inputs_returns_multiple_days(self):
        mondays_and_tuesdays = Calendary(2016).weekday((0, 1), month=7)
        mondays = [d[1] for d in mondays_and_tuesdays if d[0] == 'Monday']
        tuesdays = [d[1] for d in mondays_and_tuesdays if d[0] == 'Tuesday']
        monday_july_eighteenth = datetime.date(year=2016, month=7, day=18)
        tuesday_july_nineteenth = datetime.date(year=2016, month=7, day=19)
        assert monday_july_eighteenth in mondays
        assert tuesday_july_nineteenth in tuesdays
