import re

def convert_to_sqlite_time(time_str):
    # Regular expression to validate time format (HH:MM AM/PM)
    time_pattern = re.compile(r'^((0?[1-9]|1[0-2]):([0-5]\d)\s([AP]M))$', re.IGNORECASE)

    # Check if the input time string matches the expected format
    if not re.match(time_pattern, time_str):
        raise ValueError("Invalid time format. Time must be in 'HH:MM AM/PM' format.")

    # Split the time string into hours, minutes, and AM/PM
    match = re.match(time_pattern, time_str)
    hours, minutes, am_pm = match.group(2, 3, 4)

    # Convert hours to 24-hour format if necessary
    if am_pm.upper() == 'PM' and hours != '12':
        hours = str(int(hours) + 12)
    elif am_pm.upper() == 'AM' and hours == '12':
        hours = '00'

    # Format the time string in SQLite time format
    sqlite_time = "{:02d}:{:02d}:00".format(int(hours), int(minutes))

    return sqlite_time