import math
import calendar
class Chap6:
    def practice1(self):
        print(math.floor(-2.8))
        print(abs(round(-4.3)))
        print(math.ceil(math.sin(34.5)))

    def practice2(self):
        help(calendar.isleap())
        calendar.isleap(2016)
        dir(calendar)
        calendar.leapdays(2000, 2050)
        calendar.weekday(2016, 7, 29)

    def practice3(self, num1, num2):
        return (num1 + num2) / 2
