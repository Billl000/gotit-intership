class chap8:
    def practice1(self):
        kingdoms = ['Bacteria', 'Proto zoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
        print(kingdoms[0])
        print(kingdoms[5])
        print(kingdoms[:3])
        print(kingdoms[2:5])
        print(kingdoms[4:])
        print(kingdoms[1:0])

    def practice3(self):
        appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
        print(appointments.append('16:30'))
        print(appointments + list(('16:30')))

    def practice4(self):
        ids = ['4353', '2314', '2956', '3382', '9362', '3900']
        print(ids.remove('3382'))
        print(ids.index('9362'))
        print(ids.insert(ids.index('9362') + 1, '4499'))
        print(ids +  ['5566', '1830'])
        print(ids.reverse())
        print(ids.sort())

    def practice5(self):
        metal = [4, 12, 20, 38, 56, 88]
        print(metal[5], metal[-1])
        print(len(metal))
        print(max(metal))

    def practice6(self):
        degreeC = [16.8, 31.4, 23.9, 28, 22.5, 19.6]
        print(degreeC.sort())
        cool_temps = degreeC[0:2]
        warm_temps = degreeC[2:]
        temps_in_celsius = cool_temps + warm_temps

    def practice7(self, L):
        return L[0] == L[-1]

    def practice8(self, L1, L2):
        return len(L1) > len(L2)

    def practice10(self):
        units = [['km', 'miles', 'leagues'], ['kg', 'pound', 'stone']]
        print(units[0])
        print(units[1])
        print(units[0][0])
        print(units[1][0])
        print(units[0][1:])
        print(units[1][0:2])

chap = chap8()
print("Prac 1 : %s" % chap.practice1())
print("Prac 3 : %s" % chap.practice3())
print("Prac 4 : %s" % chap.practice4())
print("Prac 5 : %s" % chap.practice5())
print("Prac 6 : %s" % chap.practice6())
print("Prac 7 : %s" % chap.practice7([8, 8, 7, 8, 7, 8]))
print("Prac 8 : %s" % chap.practice8([5, 6, 3, 6], [4, 7, 2]))
print("Prac 10 : %s" % chap.practice10())
