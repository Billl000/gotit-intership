#practice1

class Country:
    def __init__(self, name, populations, area):
        self.name = name
        self.populations = populations
        self.area = area

    def is_larger(self, country1, country2):
        if country1.area > country2.area:
            return True
        else:
            return False

    def popular_density(self, area, populations):
        return populations / area

    def __str__(self):
        return '{} has a population of {} and is {} square km.'.format(self.name, self.population, self.area)

    def __repr__(self):
        return "Country('{0}', {1}, {2})".format(self.name, self.population, self.area)


#practice2
class Continent:
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries

        total = 0
        for country in self.countries:
            total = total + country.population
            return total

    def __str__(self):
        res = self.name
        for country in self.countries:
            res = res + '\n' + str(country)
            return res

#practice4
class Nematode:
    def __str__(self):
        return 'Nematode: {}mm long, gender is {}, {} days old'.format(self.length, self.gender, self.age)

    def __repr__(self):
        return "Nematode({}, '{}', {})".format(self.length, self.gender, self.age)

#practice5a
class Point:
    def __init__(self, x, y,):
        self.x = x
        self.y = y

#practice5b
class LineSegment:
    def __init__(self, point1, point2):
        self.startpoint = point1
        self.endpoint = point2

#pracitce5c
    def slope(self):
        return (self.endpoint.y - self.startpoint.y) / (self.endpoint.x - self.startpoint.x)

#practice5d
    def length(self):
        return math.sqrt((self.endpoint.x(self.endpoint.y - self.startpoint.x) ** 2 + - self.startpoint.y) ** 2)

