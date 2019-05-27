class chap9:
    def practice1(self):
        str phenotype
        celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
        for phenotype in celegans_phenotypes:
            print (phenotype)

    def practice2(self):
        half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
        for value in half_lives:
            print(value, end = ' ')

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
            number_and_weight.append(inner_list[0]) number_and_weight.append(inner_list[1])
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
        for population in country_populations:
            total += population

    def practice8(self):
        if rat_1[0] > rat_2[0]:
            print("Rat 1 weighed more than rat 2 on day 1")
        else:
            print("Rat 1 weighed less than rat 2 on day 1")

        if rat_1[0] > rat_2[0] and rat_1[-1] > rat_2[-1]:
            print("Rat 1 remained heavier than 2 on day 1.")
        else
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
            print(10 - number, end=' ')

    def practice11(self):
        sum = 0
        i = 0
        for number in range(2, 23):
            sum += number
            i += 1
        average = sum / i
        print(average)

    def practice12(self):
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
            print(' ' * (7 - width), 'T' * width, sep='')

    def practice15(self):
        width = 1
        while width < 8:
            print('T' * width)
            width += 1
        width = 1
        while width < 8:
            print(' ' * (7 - width), 'T' * width, sep='')
            width += 1

    def practice16(self):
        week = 1
        while rat_1_weight[week] / rat_1_weight[0] - 1 < .25:
            week += 1
            print(week)

        week = 0
        while rat_1_weight[week] / rat_2_weight[week] - 1 < .10:
            week += 1
            print(week)