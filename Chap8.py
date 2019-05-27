class chap8:
    def practice1(self):
        kingdoms = ['Bacteria', 'Proto zoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
        print(kindoms[0])
        print(kingdoms[5])
        print(kingdoms[;3])
        print(kingdoms[2:5])
        print(kingdoms[4:])
        print(kingdoms[1:0])

    def practice3(self):
        appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
        print(appointments.append('16:30'))
        print(appointments += '16:30')

    def practice4(self):
        ids = ['4353', '2314', '2956', '3382', '9362', '3900']
        print(ids.remove('3382'))
        print(ids.index('9362'))
        print(ids.insert(ids.index('9362') + 1, '4499'))
        print(ids = ids + ['5566', '1830'])
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
        

