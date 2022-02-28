def add_time(start, duration, day=None):
    start_elements = []
    unit = ""
    days = 0
    if (day):
        if day.lower() == "monday":
            day = "Monday"
        elif day.lower() == "tuesday":
            day = "Tuesday"
        elif day.lower() == "wednesday":
            day = "Wednesday"
        elif day.lower() == "thursday":
            day = "Thursday"
        elif day.lower() == "friday":
            day = "Friday"
        elif day.lower() == "saturday":
            day = "Saturday"
        else:
            day = "Sunday"
    if len(start) == 7:
        start_elements.append(int(start[0]))
        start_elements.append(int(start[2:4]))
        unit = start[5:]
    elif len(start) == 8:
        start_elements.append(int(start[0:2]))
        start_elements.append(int(start[3:5]))
        unit = start[6:]
    duration_elements = duration.split(":")
    duration_elements[0] = int(duration_elements[0])
    duration_elements[1] = int(duration_elements[1])
    for i in range(0, duration_elements[1]):
        start_elements[1] += 1
        if start_elements[1] == 60:
            start_elements[0] += 1
            start_elements[1] = 0
            if start_elements[0] == 12:
                if unit == "PM":
                    days += 1
                    unit = "AM"
                    if day:
                        day = advance_day(day)
                else:
                    unit = "PM"
            if start_elements[0] == 13:
                start_elements[0] = 1
    for i in range(0, duration_elements[0]):
        start_elements[0] += 1
        if start_elements[0] == 12:
            if unit == "PM":
                days += 1
                unit = "AM"
                if day:
                    day = advance_day(day)
            else:
                unit = "PM"
        if start_elements[0] == 13:
            start_elements[0] = 1
    return_minutes = format(str(start_elements[1]), "0>2")
    return_string = (
        str(start_elements[0]) + ":" + return_minutes + " " + str(unit)
    )
    if day:
        return_string += ", " + day
    if days == 1:
        return_string += " (next day)"
    elif days > 0:
        return_string += " (" + str(days) + " days later)"
    return return_string


def advance_day(current_day):
    if current_day == "Monday":
        return "Tuesday"
    elif current_day == "Tuesday":
        return "Wednesday"
    elif current_day == "Wednesday":
        return "Thursday"
    elif current_day == "Thursday":
        return "Friday"
    elif current_day == "Friday":
        return "Saturday"
    elif current_day == "Saturday":
        return "Sunday"
    elif current_day == "Sunday":
        return "Monday"

