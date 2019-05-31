class chap11:
    @property
    def practice1(self):
        repeat = 1
        find_dups = []
        dups = set()
        index = input("How many numbers would you like to add?")
        print("Enter your number: ")
        for i in range(index):
            num = input()
            find_dups.append(num)

        for x in range(index):
            for y in range(index-1):
                if (find_dups[x] == find_dups[y]):
                    repeat = repeat + 1
                    if repeat > 2:
                        dups.add(find_dups[x])
                        break
        return dups

    def practice2(self, males, females):
        pairs = set()
        num_gerbils = len(males)
        for i in range(num_gerbils):
            male = males.pop()
            female = females.pop()
            pairs.add((male, female))

        return pairs

    def practice3(self, filenames):
        authors = set()
        for filename in filenames:
            filename = open(filenames)
            for line in filename:
                if line.lower().startswith('author'):
                 author = line[6:].strip()
                authors.add(author)

        return authors

    def practice4(self, dictionary):
        return len(set(dictionary.values()))

    def practice5(self, dictionary):
        smallest = 1
        name = ''

        for particle in dictionary:
            probability = dictionary[particle]
            if probability < smallest:
                smallest = probability
                name = particle

        return particle

    def practice6(self, dictionary):
        duplicates = 0
        values = list(dictionary.values())
        for item in values:
            duplicates = duplicates + 1
            values.remove(item)

        return duplicates

    def practice7(self, color_dict):
        sum = 0
        for i in color_dict:
            sum = color_dict[i] + sum

        return sum == 1.0

    def practice8(self, dict1, dict2):
        intersection = {}
        for (key, value) in dict1.items():
            if key in dict2 and value == dict2[key]:
                intersection[key] = value
        return intersection

    def practice9(self, dict_of_dict):
        inner_keys = set()
        for key in dict_of_dict:
            for inner_key in dict_of_dict[key]:
                inner_keys.add(inner_key)
        
        return inner_keys
        
    def practice10(self, dict_of_dict):
        inner_keys_list = []
        for key in dict_of_dict:
            inner_keys = list(dict_of_dict[key].keys())
            inner_keys.sort()
            inner_keys_list.append(inner_keys)
        for i in range(1, len(inner_keys_list)):
            if len(inner_keys_list[0]) != len(inner_keys_list[i]):
                return False

        for j in range(len(inner_keys_list[0])):
            if inner_keys_list[0][j] != inner_keys_list[i][j]:
                return False

        return True
    def practice11a(self, vector1, vector2):
        sum_vector = vector1.copy()
        for key in vector2:
            if key in sum_vector:
                sum_vector[key] = sum_vector[key] + vector2[key]
            else:
                sum_vector[key] = vector2[key]
        return sum_vector

    def practice11b(self, vector1, vector2):
        dot = 0
        for key1 in vector1:
            if key1 in vector2:
                dot = dot + vector1[key1] * vector2[key1]
        return dot


chapter = chap11()

print("Prac 1: %s" % chapter.practice1)
print("Prac 2: %s" % chapter.practice2({'Anne', 'Beatrice', 'Cari'}, {'Ali', 'Bob', 'Chen'}))
print("Prac 3: %s" % chapter.practice3("ex3_data.edb"))
print("Prac 4: %s" % chapter.practice4({'red': 1, 'green': 1, 'blue': 2}))
print("Prac 5: %s" % chapter.practice5({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07}))
print("Prac 6: %s" % chapter.practice6({'R': 1, 'G': 2, 'B': 2, 'Y': 1, 'P': 3}))
print("Prac 7: %s" % chapter.practice7({'R': 0.5, 'G': 0.4, 'B': 0.7}))
print("Prac 8: %s" % chapter.practice8({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'd': 2, 'b': 2}))
print("Prac 9: %s" % chapter.practice9({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}}))
print("Prac 10: %s" % chapter.practice10({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}}))
print("Prac 11: %s" % chapter.practice11a({1: 3, 3: 4}, {2: 4, 3: 5,5: 6}))
print("Prac 11: %s" % chapter.practice11b({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6}))





