class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days_of_week[datetime.datetime(year, month, day).weekday()]