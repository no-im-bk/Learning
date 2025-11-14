# Not the best way to keep track of the number of days per month
# But I want to play with these special methods
class MonthData:
    _dayArray = [31,28,31,30,31,30,31,31,30,31,30,31]
    _monthNameArray = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    def __getitem__(self, i):
        return (self._dayArray[i],self._monthNameArray[i])

class Date:
    _monthData = MonthData()
    def __init__(self,month,day):
        self._day = day
        self._month = month

    def __repr__(self):
        return f"Date({self._month},{self._day})"
    
    def __str__(self):
        (_,month) = self._monthData[self._month]
        return f"{month} {self._day + 1}"
    
    def __add__(self, daysToAdd):
        day = self._day + daysToAdd
        month = self._month
        while day >= self._monthData[month][0]:
            day -= self._monthData[month][0]
            month = (month + 1) % 12
        return Date(month,day)

d = Date(0,0)
print("Set date to Jan 1st:")
print(f"d = {d}")
d = d + 20
print("Add 20 days. Expect Jan 21st:")
print(f"d = {d}")
d = d + 20
print("Add 20 days. Expect Feb 10th:")
print(f"d = {d}")
d = d + 366
print("Add 366 days. Expect Feb 11th:")
print(f"d = {d}")



        

    
