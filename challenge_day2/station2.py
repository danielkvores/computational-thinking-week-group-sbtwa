# year-month-day input that return the day of the year in japanese
from datetime import date
def solution_station_2(date_string):
    def english_day():
        return date.fromisoformat(date_string).strftime("%A")
    
    if english_day() == "Monday":
        return "月曜日"
    elif english_day() == "Tuesday":
        return "火曜日"
    elif english_day() == "Wednesday":
        return "水曜日"
    elif english_day() == "Thursday":
        return "木曜日"
    elif english_day() == "Friday":
        return "金曜日"
    elif english_day() == "Saturday":
        return "土曜日"
    elif english_day() == "Sunday":
        return "日曜日"
