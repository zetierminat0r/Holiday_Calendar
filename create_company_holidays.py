import sys
from datetime import datetime, timedelta
import calendar

# Finds the nth weekday of the month.
def find_nth_weekday(year, month, target_weekday, nth_week):
    month_first_day = datetime(year, month, 1)
    first_day_weekday = month_first_day.weekday()
    delta_days = (target_weekday - first_day_weekday) % 7
    target_date = month_first_day + timedelta(days=delta_days + 7 * (nth_week - 1))
    return target_date

# Finds the last specific weekday of the month.
def last_weekday_of_month(year, month, target_weekday):
    last_day_of_month = calendar.monthrange(year, month)[1]
    month_last_day = datetime(year, month, last_day_of_month)
    weekday = month_last_day.weekday()
    delta_days = (weekday - target_weekday) % 7
    return month_last_day - timedelta(days=delta_days)

def calculate_holiday_date(year, holiday):
    if holiday.endswith("Martin Luther King Jr. Day"):           return find_nth_weekday(year, 1, 0, 3)
    elif holiday.endswith("Presidents' Day"):                    return find_nth_weekday(year, 2, 0, 3)
    elif holiday.endswith("Memorial Day"):                       return last_weekday_of_month(year, 5, 0)
    elif holiday.endswith("Labor Day"):                          return find_nth_weekday(year, 9, 0, 1)
    elif holiday.endswith("Columbus Day"):                       return find_nth_weekday(year, 10, 0, 2)
    elif holiday.endswith("Thanksgiving Day"):                   return find_nth_weekday(year, 11, 3, 4)
    elif holiday.endswith("New Year's Day"):                     return datetime(year, 1, 1)
    elif holiday.endswith("Juneteenth National Independence Day"): return datetime(year, 6, 19)
    elif holiday.endswith("Independence Day"):                   return datetime(year, 7, 4)
    elif holiday.endswith("Veterans Day"):                       return datetime(year, 11, 11)
    elif holiday.endswith("Christmas Day"):                      return datetime(year, 12, 25)
    else:
        return None

def create_calendar_entries(start_year, num_years, holidays, company_name):
    entries = []
    for year in range(start_year, start_year + num_years):
        for holiday in holidays:
            holiday_name = f"{company_name} Observed {holiday}"
            holiday_date = calculate_holiday_date(year, holiday_name)
            if holiday_date:
                entry = {'date': holiday_date, 'name': holiday_name}
                entries.append(entry)
    return entries

def create_ics_content(entries):
    ics_content = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Custom Holiday Calendar//mxm.dk//"]
    for entry in entries:
        event = [
            "BEGIN:VEVENT",
            f"DTSTART:{entry['date'].strftime('%Y%m%d')}",
            f"DTEND:{(entry['date'] + timedelta(days=1)).strftime('%Y%m%d')}",
            f"SUMMARY:{entry['name']}",
            "END:VEVENT"
        ]
        ics_content.extend(event)
    ics_content.append("END:VCALENDAR")
    return "\n".join(ics_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_company_holidays.py <company name> <number of years of entries>")
        sys.exit(1)

    company_name = sys.argv[1]
    num_years = int(sys.argv[2])

    # Define a base list of holidays, you may expand or customize this list as needed.
    holidays = [
        "New Year's Day",
        "Martin Luther King Jr. Day",
        "Presidents' Day",
        "Memorial Day",
        "Independence Day",
        "Labor Day",
        "Columbus Day",
        "Veterans Day",
        "Thanksgiving Day",
        "Christmas Day"
    ]

    start_year = datetime.now().year
    entries = create_calendar_entries(start_year, num_years, holidays, company_name)
    ics_content = create_ics_content(entries)

    # Define the output file name dynamically based on the company name.
    ics_file_path = f'{company_name.replace(" ", "_").lower()}_holidays.ics'
    with open(ics_file_path, 'w') as file:
        file.write(ics_content)

    print(f"ICS file created: {ics_file_path}")

