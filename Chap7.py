class chap7:
    def practice1(self):
        print('hello'.upper())
        print('Happy Birthday!'.lower())
        print('WeeeEEEEeeeEEEEeee'.swapcase())
        print('ABC123'.isupper())
        print('aeiouAEIOU'.count('a'))
        print('hello'.endswith('o'))
        print('hello'.startswith('H'))
        print('Hello {0}'.format('Python'))
        print('Hello {0}! Hello {1}!'.format('Python', 'World'))

    def practice2(self):
        print('tomato'.count('o'))

    def practice3(self):
        print('tomato'.find('o'))

    def practice4(self):
        print('tomato'.find('o', 'tomato'.find('o') + 1))

    def practice5(self):
        print('avocado'.find('o', 'avocado'.find('o') + 1))

    def practice6(self):
        print('runner'.replace('n', 'b'))

    def practice7(self):
        str s = ' yes   '
        print(s.strip(' '))

    def practice8(self):
        str fruit = 'pineapple'
        print(fruit.find('p', fruit.count('p')))
        print(fruit.count(fruit.upper().swapcase()))
        print(fruit.replace(fruit.swapcase(), fruit.lower()))

    def practice9(self):
        str season = 'summer'
        print('I love '.join(season))

    def practice10(self):
        int side1 = 3
        int side2 = 4
        int side3 = 5
        print('The sides have length {0}, {1}, and {2}'.format(side1, side2, side3))

    def practice11(self):
        print('boolean'.capitalize())
        print('CO2 H2O'.find('2'))
        print('CO2 H2O'.find('2', 'CO2 H2O'.find('2' + 1)))
        print('Boolean'[0].islower())
        print('MoNDaY'.lower().capitalize())
        print('  Monday'.lstrip())

    def practice12(self, s1, s2, ch):

        return s1.count(ch) + s2.count(ch)
