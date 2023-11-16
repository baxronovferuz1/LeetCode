class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = date.fromisoformat(date1)
        d2 = date.fromisoformat(date2)
        td = d1 - d2
        return abs(td.days)
        