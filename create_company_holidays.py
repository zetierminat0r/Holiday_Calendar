from datetime import datetime, timedelta
import calendar

#Finds the nth weekday of the month.
def find_nth_weekday(year, month, target_weekday, nth_week):
    month_first_day = datetime(year, month, 1)
    first_day_weekday = month_first_day.weekday()
    delta_days = (target_weekday - first_day_weekday) % 7
    target_date = month_first_day + timedelta(days=delta_days + 7 * (nth_week - 1))
    return target_date

#Finds the last specific weekday of the month.
def last_weekday_of_month(year, month, target_weekday):
    last_day_of_month = calendar.monthrange(year, month)[1]
    month_last_day = datetime(year, month, last_day_of_month)
    weekday = month_last_day.weekday()
    delta_days = (weekday - target_weekday) % 7
    return month_last_day - timedelta(days=delta_days)

#Calculates the date of a given holiday for the specified year.
def calculate_holiday_date(year, holiday):
    holiday = holiday.replace("Zetier Holiday - ", "")
    if   holiday == "Martin Luther King Jr. Day":           return find_nth_weekday(year, 1, 0, 3)  # 3rd Monday in January
    elif holiday == "Presidents' Day":                      return find_nth_weekday(year, 2, 0, 3)  # 3rd Monday in February
    elif holiday == "Memorial Day":                         return last_weekday_of_month(year, 5, 0)  # Last Monday in May
    elif holiday == "Labor Day":                            return find_nth_weekday(year, 9, 0, 1)  # 1st Monday in September
    elif holiday == "Columbus Day":                         return find_nth_weekday(year, 10, 0, 2)  # 2nd Monday in October
    elif holiday == "Thanksgiving Day":                     return find_nth_weekday(year, 11, 3, 4)  # 4th Thursday in November
    elif holiday == "New Year's Day":                       return datetime(year, 1, 1)
    elif holiday == "Juneteenth National Independence Day": return datetime(year, 6, 19)
    elif holiday == "Independence Day":                     return datetime(year, 7, 4)
    elif holiday == "Veterans Day":                         return datetime(year, 11, 11)
    elif holiday == "Christmas Day":                        return datetime(year, 12, 25)
    else:
        return None

def create_calendar_entries(start_year, num_years, holidays):
    entries = []
    for year in range(start_year, start_year + num_years):
        for holiday in holidays:
            holiday_date = calculate_holiday_date(year, holiday)
            if holiday_date:
                entry = {'date': holiday_date, 'name': holiday}
                entries.append(entry)
                print(f"Added entry: {entry}")  # Debug print
    return entries

def create_ics_content(entries):
    ics_content = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Zetier Holiday Calendar//mxm.dk//"]
    for entry in entries:
        event = [
            "BEGIN:VEVENT",
            f"DTSTART:{entry['date'].strftime('%Y%m%d')}",
            f"DTEND:{(entry['date'] + timedelta(days=1)).strftime('%Y%m%d')}",
            f"SUMMARY:{entry['name']}",
            "END:VEVENT"
        ]
        ics_content.extend(event)
        print(f"Added event: {event}")  # Debug print
    ics_content.append("END:VCALENDAR")
    return "\n".join(ics_content)


# Define the holidays
holidays = [
    "Zetier Holiday - Martin Luther King Jr. Day",
    "Zetier Holiday - Presidents' Day",
    "Zetier Holiday - Memorial Day",
    "Zetier Holiday - Labor Day",
    "Zetier Holiday - Columbus Day",
    "Zetier Holiday - Thanksgiving Day",
    "Zetier Holiday - New Year's Day",
    "Zetier Holiday - Juneteenth National Independence Day",
    "Zetier Holiday - Independence Day",
    "Zetier Holiday - Veterans Day",
    "Zetier Holiday - Christmas Day"
]


# Generate the entries
entries = create_calendar_entries(datetime.now().year, 20, holidays)

# Create the ICS content
ics_content = create_ics_content(entries)

# Write to a file
ics_file_path = 'zetier_holidays.ics'
with open(ics_file_path, 'w') as file:
    file.write(ics_content)

print(f"ICS file created: {ics_file_path}")


