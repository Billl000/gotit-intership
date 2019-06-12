import math
import calendar
class Chap6:
    def practice1(self):
        print(math.floor(-2.8))
        print(abs(round(-4.3)))
        print(math.ceil(math.sin(34.5)))

    def practice2(self):
        help(calendar.isleap(2016))
        calendar.isleap(2016)
        dir(calendar)
        calendar.leapdays(2000, 2050)
        calendar.weekday(2016, 7, 29)

    def practice3(self, num1, num2):
        return (num1 + num2) / 2

chap = Chap6()
print("Practice 1: %s" %chap.practice1())
print("Practice 2: %s" %chap.practice2())
print("Practice 3: %s" %chap.practice3(6 , 8))
