Get discord time codes from Avrae.
With no arguments it creates a relative time code for the moment it was run.

Syntax ``!time [-arg1] [additional args]``
Any number or order of the arguments is permaitted. Only the last value of an argument will be taken if multiple of the same argument exist.

__Arguments__
All the arguments below can be abbreviated as their first letter, ***except*** ``hours`` (due to a Avrae argument name restriction). The abbreviation for it is  ``hr``


``-time <# UNIX time>`` The time to base the time code on. Any adjustments to time units (see below) are done to this time. If not included, the time used is when you used the alias. This number is the UNIX time system, the same number in the center of a discord time code. Examples: ``-time 1672531200``   ``-t -22075200``
``-seconds <# seconds>``, ``-minutes <# minutes>``, ``-hours <# hours>``, ``-days <# days>``,  ``-weeks <# weeks>`` Add or subtract a number of that time unit from the time code you want to generate. Including an addtion sign is accepted but not required. Examples: ``!time -days 3`` would make a time code for three days from now, ``!time -w -1 -hr 2`` would make a time code for three weeks before to an hour from now.
``-years <# years>`` Add or subtract years to the time code. Same syntax as the other time units. Note this is simply 365 days, not an exact year that would account for leap seconds or leap years. The higher the change the more you will get time drifting.
``-round <time unit>`` Rounds down to the nearest time unit, using the same argument word or abbreviation as the units above. Rounding for all units is based on midnight UTC, which is <t:1672617600:t> your time. The same time drifting issue applies to rounding by years. Examples ``!time -hours 3 -round hours`` makes a time code to the start of the hour of three hours from now, ``!time -r m`` gives you the start of the minute you used it.
``-format <letter code>`` The format of the generated time code. The discord time formats letter codes with their resulting displays: d <t:1672617600:d>, D <t:1672617600:D>, t <t:1672617600:t>, T <t:1672617600:T>, f <t:1672617600:f>, F <t:1672617600:F>, R <t:1672617600:R>. As an addtional option is to enter dt or DT to get a D time code followed by a space and a T time code. The default if left blank is the R code. Examples ``!time -format T``   ``!time -f dt``
``v`` See detailed information on the generation of the time code, such as parameters used.
``i`` Ignore your active user settings. (A command to set user settings has not been made yet)
