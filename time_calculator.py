"""
Build a Time Calculator Project
Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
"""

def add_time(start, duration, day=None):

    new_time = None
    hr_mins = 60

    days_of_the_week = [
        "monday", 
        "tuesday", 
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
    ]

    time_dict= {
        "start": {
            "hr": None, 
            "min": None, 
            "std": None
        },
        "duration": {
            "hr": None, 
            "min": None
        },
        "new_time": {
            "hr": 0, 
            "min": 0, 
            "std": None,
            "days": 0,
            "day": None
        }
    }

    start_am_pm_split = start.split(" ")
    start_hr_min_split = start_am_pm_split[0].split(":")

    time_dict["start"]["hr"] = start_hr_min_split[0]
    time_dict["start"]["min"] = start_hr_min_split[1]
    time_dict["start"]["std"] = start_am_pm_split[1]

    duration_am_pm_split = duration.split(" ")
    duration_hr_min_split = duration_am_pm_split[0].split(":")

    time_dict["duration"]["hr"] = duration_hr_min_split[0]
    time_dict["duration"]["min"] = duration_hr_min_split[1]

    start_min = (int(time_dict["start"]["hr"]) * 60) + int(time_dict["start"]["min"])

    borrowed_time = ((int(time_dict["start"]["hr"])+1) * 60) - start_min

    time_dict["new_time"]["hr"] = int(time_dict["start"]["hr"])
    time_dict["new_time"]["std"] = time_dict["start"]["std"]

    # Set day of the week
    day_index = None

    if day:
        day = day.lower()
    
        if day in days_of_the_week:
            day_index = days_of_the_week.index(day)

    time_dict["new_time"]["day"] = day_index

    # Set duration and remaining time
    duration_mins = (int(time_dict["duration"]["hr"]) * 60) + int(time_dict["duration"]["min"])

    remaining_time = duration_mins - borrowed_time

    if duration_mins == 0:
        remaining_time = 0
    
        time_dict["new_time"]["min"] = int(time_dict["start"]["min"])
    else:
        time_dict["new_time"]["hr"] += 1

        if time_dict["new_time"]["hr"] == 12: 
            if time_dict["new_time"]["std"] == "PM":
                time_dict["new_time"]["std"] = "AM"
            elif time_dict["new_time"]["std"] == "AM":
                time_dict["new_time"]["std"] = "PM"

        if remaining_time < 60:
            time_dict["new_time"]["min"] = remaining_time

        while remaining_time > 60:

            if time_dict["new_time"]["hr"] <= 12:
                time_dict["new_time"]["hr"] += 1
            
            if time_dict["new_time"]["hr"] == 13:
                time_dict["new_time"]["hr"] = 1

            if time_dict["new_time"]["hr"] == 12: 
                if time_dict["new_time"]["std"] == "PM":
                    time_dict["new_time"]["std"] = "AM"
                elif time_dict["new_time"]["std"] == "AM":
                    time_dict["new_time"]["std"] = "PM"

            remaining_time -= 60
            start_min += 60 

            if remaining_time < 60:
                time_dict["new_time"]["min"] = remaining_time

            if start_min >= 720 and time_dict["new_time"]["std"] == "AM":
                time_dict["new_time"]["days"] += 1
                start_min = 1

                if time_dict["new_time"]["day"] is not None:
                    if time_dict["new_time"]["day"] >= 6:
                        time_dict["new_time"]["day"] = 0
                    else:
                        time_dict["new_time"]["day"] += 1

                    # print(time_dict["new_time"]["day"], time_dict)

    # Minutes Padding with 0
    if int(time_dict["new_time"]["min"]) < 9:
        time_dict["new_time"]["min"] = f'0{str(time_dict["new_time"]["min"])}'
        
    # Days Calculations
    day = ""
    if time_dict["new_time"]["days"] == 1:
        day = "(next day)"
    
    if time_dict["new_time"]["days"] > 1:
        day = f'({time_dict["new_time"]["days"]} days later)'

    # Setting new

    if time_dict["new_time"]["day"] is not None and day == "":
        new_time = f'{str(time_dict["new_time"]["hr"])}:{str(time_dict["new_time"]["min"])} {time_dict["new_time"]["std"]}, {days_of_the_week[time_dict["new_time"]["day"]].title()}'
    elif time_dict["new_time"]["day"] is not None and day != "":
        new_time = f'{str(time_dict["new_time"]["hr"])}:{str(time_dict["new_time"]["min"])} {time_dict["new_time"]["std"]}, {days_of_the_week[time_dict["new_time"]["day"]].title()} {day}'
    elif time_dict["new_time"]["day"] is None and day != "":
        new_time = f'{str(time_dict["new_time"]["hr"])}:{str(time_dict["new_time"]["min"])} {time_dict["new_time"]["std"]} {day}'
    elif time_dict["new_time"]["day"] is None and day == "":
        new_time = f'{str(time_dict["new_time"]["hr"])}:{str(time_dict["new_time"]["min"])} {time_dict["new_time"]["std"]}'

    return new_time


print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)