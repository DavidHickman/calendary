===============================
calendary
===============================


.. image:: https://img.shields.io/pypi/v/calendary.svg
        :target: https://pypi.python.org/pypi/calendary

.. image:: https://travis-ci.org/DavidHickman/calendary.svg?branch=master
    :target: https://travis-ci.org/DavidHickman/calendary

.. image:: https://readthedocs.org/projects/calendary/badge/?version=latest
        :target: https://calendary.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/davidhickman/calendary/shield.svg
     :target: https://pyup.io/repos/github/davidhickman/calendary/
     :alt: Updates

.. image:: https://pyup.io/repos/github/davidhickman/calendary/python-3-shield.svg
     :target: https://pyup.io/repos/github/davidhickman/calendary/
     :alt: Python 3


Python calendar and datetime helpers.


* Free software: BSD license
* Documentation: https://calendary.readthedocs.io.


Features
--------

Return a list of days for any year

.. code-block:: python

    cal = Calendary(2016)

    weekdays = cal.weekday_calendar()
    today = datetime.datetime.now().date()

    for weekday, date in weekdays:
        if date < today:
            print("{0}-{1}-{2} was a {3}".format(date.month, date.day, date.year, weekday))
        elif date == today:
            print("Today is {}".format(weekday))
        else:
            print("{0}-{1}-{2} will be a {3}".format(date.month, date.day, date.year, weekday))


Return a list of only workdays (default: Monday-Friday)

.. code-block:: python

    cal = Calendary(2016)

    workdays = cal.workday_calendar()

    for weekday, date in workdays:
        print(weekday, date)


Change the workweek begin and end

.. code-block:: python

    cal = Calendary(2016)

    # Work Tuesday - Saturday
    workdays = cal.workday_calendar(workweek_start=1, workweek_end=5)


Get the calendar for a specific month

.. code-block:: python

    cal = Calendary(2016)

    # July calendar
    cal.month(7)

    # July workweek calendar
    cal.month(7, work=True, workweek_start=1, workweek_end=5)


Get a specific date relative to the calendar

.. code-block:: python

    cal = Calendary(2016)

    # Get the third Thursday in July of 2016
    cal.weekday('Thursday', month=7, ordinal=3)

    # Get all Thursdays in July 2016
    cal.weekday('Thursday', month=7)

    # Get the third Thursday in 2016
    cal.weekday('Thursday', ordinal=3)

    # Get all Thursdays in 2016
    cal.weekday('Thursday')


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
