from utils.display import display_chap_result

class chap4():
    def practice1(self):
        print ('Computer' + 'Science')
        print ('Darwin\s')
        print ('H2O' * 3)
        print ('CO2' * 0)

    def practice2(self):
        print("They'll hibernate during the winter.")
        print('"Absolutely not," he said.')
        print('''"He said, 'Absolutely not'", recalled Mel''')
        print("hydrogen sulfide")
        print("Left" + "'" + "right")

    def practice3(self):
        print("'''A")
        print("B")
        print("C'''")

    def practice4(self):
        a = ""
        print(len(a))

    def practice5(self):
        x = 3
        y = 12.5
        print("The rabbit is " + str(x))
        print("The rabbit is " + str(x) + " years old")
        print(str(y) + " is average")
        print(str(y) + " * " + str(x))
        print(str(y) + " * " + "3" + " is " + str((y * x)))

    def practice7(self):
        i = input()
        return float

    def practice8(self, index1, index2):
        if index2 > 0:
            for i in range(index2):
                print(index1)
        else :
            return ""

    def practice9(self, s1, s2):
        return sum(len(s1) + len(s2))

challenge = chap4()

# display_chap_result("1", challenge.practice1())
# display_chap_result("2", challenge.practice2())

print("Practice 1: %s" % challenge.practice1())
print("Practice 2: %s" % challenge.practice2())
print("Practice 3: %s" % challenge.practice3())
print("Practice 4: %s" % challenge.practice4())
print("Practice 5: %s" % challenge.practice5())
print("Practice 7: %s" % challenge.practice7())
print("Practice 8: %s" % challenge.practice8(4, 5))
print("Practice 9: %s" % challenge.practice9('faid', 'kaow'))

