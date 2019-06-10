class chap9:
    def practice1(self):
        phenotype = ''
        celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
        for phenotype in celegans_phenotypes:
            print (phenotype)

    def practice2(self):
        end = ' '
        half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
        for value in half_lives:
            print(value)

    def practice3(self):
        whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
        more_whales = []
        for count in whales:
            more_whales.append(count + 1)

    def practice4(self):
        alkaline_earth_metals = [[4, 9.012], [12, 24.305], [20, 40.078], [38, 87.62], [56, 137.327], [88, 226]]
        for inner_list in alkaline_earth_metals:
            print(inner_list[0])
            print(inner_list[1])

        number_and_weight = []
        for inner_list in alkaline_earth_metals:
            number_and_weight.append(inner_list[0])
            number_and_weight.append(inner_list[1])
        print('end')

    def practice6(self):
        text = ""
        while text.lower() != "quit":
            text = input("Please enter a chemical formula (or 'quit' to exit): ")
            if text == "quit":
                print("...exiting program")
            elif text == "H2O":
                print("Water")
            elif text == "NH3":
                print("Ammonia")
            elif text == "CH4":
                print("Methane")
            else:
                print("Unknown compound")

    def practice7(self):
        total = 0
        country_populations = [1295, 23, 7, 3, 47, 21]
        for population in country_populations:
            total += population

    def practice8(self, rat_1, rat_2):
        if rat_1[0] > rat_2[0]:
            print("Rat 1 weighed more than rat 2 on day 1")
        else:
            print("Rat 1 weighed less than rat 2 on day 1")

        if rat_1[0] > rat_2[0] and rat_1[-1] > rat_2[-1]:
            print("Rat 1 remained heavier than 2 on day 1.")
        else:
            print("Rat 2 became heavier than Rat 1.")
            if rat_1[0] > rat_2[0]:
                if rat_1[-1] > rat_2[-1]:
                    print("Rat 1 remained heavier than Rat 2.")
                else:
                    print("Rat 2 became heavier than Rat 1.")
            else:
                print("Rat 2 became heavier than Rat 1.")

    def practice9(self):
        for number in range(33, 50):
            print(number)

    def practice10(self):
        for number in range(10):
            print(10 - number)

    def practice11(self):
        sum = 0
        i = 0
        for number in range(2, 23):
            sum += number
            i += 1
        average = sum / i
        print(average)

    def practice12(self, num_list):
        index = 0
        while index < len(num_list):
            if num_list[index] < 0:
                del num_list[index]
            else:
              index += 1

    def practice13(self):
        for width in range(1, 8):
            print('T' * width)

    def practice14(self):
        for width in range(1, 8):
            print(' ' * (7 - width), 'T' * width)

    def practice15(self):
        width = 1
        while width < 8:
            print('T' * width)
            width += 1
        width = 1
        while width < 8:
            print(' ' * (7 - width), 'T' * width)
            width += 1

    def practice16(self, rat_1_weight, rat_2_weight):
        week = 1
        while rat_1_weight[week] / rat_1_weight[0] - 1 < .25:
            week += 1
            print(week)

        week = 0
        while rat_1_weight[week] / rat_2_weight[week] - 1 < .10:
            week += 1
            print(week)

chap = chap9()
print("Prac 1 : %s" % chap.practice1())
print("Prac 2 : %s" % chap.practice2())
print("Prac 3 : %s" % chap.practice3())
print("Prac 4 : %s" % chap.practice4())
print("Prac 6 : %s" % chap.practice6())
print("Prac 7 : %s" % chap.practice7())
print("Prac 8 : %s" % chap.practice8([6, 7, 8], [9, 9, 7]))
print("Prac 9 : %s" % chap.practice9())
print("Prac 10 : %s" % chap.practice10())
print("Prac 11 : %s" % chap.practice11())
print("Prac 12 : %s" % chap.practice12([-4, 5, -7, -9, 2 ]))
print("Prac 13 : %s" % chap.practice13())
print("Prac 14 : %s" % chap.practice14())
print("Prac 15 : %s" % chap.practice15())
print("Prac 16 : %s" % chap.practice16([7, 8, 12, 5], [6, 7, 23, 4]))
