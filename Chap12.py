class chap12:
    def practice1(self, sequence):
        complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        sequence_complement = ''
        for char in sequence:
            sequence_complement = sequence_complement + complement_dict[char]
        return sequence_complement

    def practice2a(self, L):
        index = 0
        smallest = L[0]
        for i in range(1, len(L)):
            if L[i] < smallest:
                index = i
            smallest = L[i]
        return index

    def practice2b(self, L):
        index = 0
        smallest = L[0]
        for i in range(1, len(L)):
            if L[i] < smallest:
                index = i
                smallest = L[i]
        return smallest, index

    def practice2c(self, L, flag):
        index = 0
        current_value = L[0]
        if flag:
            for i in range(1, len(L)):
                if L[i] < current_value:
                    index = i
                    current_value = L[i]
        else:
            for i in range(1, len(L)):
                if L[i] > current_value:
                    index = i
                    current_value = L[i]
        return (current_value, index)

    def practice3b(self, filename):
        with open(filename, 'r') as hopedale_file:
            data = hopedale_file.readline().strip()
            while data.startswith('#'):
                data = hopedale_file.readline().strip()
            pelts_list = []
            pelts_list.append(int(data))
            pelts_list.append(int(data.strip()))

            for data in hopedale_file:
                pelts_list.append(int(data.strip()))
        return sum(pelts_list) / len(pelts_list)

    def practice6(self, color_list):
        i = 0
        start_green = 0
        start_unknown = 0
        end_unknown = len(color_list) - 1
        while start_unknown <= end_unknown:

            if color_list[start_unknown] == 'red':
                color_list[start_green], color_list[start_unknown] = color_list[start_unknown],color_list[start_green]
                start_green += 1
                start_unknown += 1
            elif color_list[start_unknown] == 'green':
                start_unknown += 1
            else:
                color_list[start_unknown], color_list[end_unknown] = color_list[end_unknown], color_list[start_unknown]
                end_unknown -= 1

        print(color_list)

chapter = chap12()

print("Prac 1 : %s" % chapter.practice1("ATTGCGCTTA"))
print("Prac 2a: %s" % chapter.practice2a([1, 8, 9, 6, 3, 5]))
print("Prac 2b : {}".format(chapter.practice2b([4, 3, 2, 4, 3, 6, 1, 5])))
print("Prac 2c : {}".format( chapter.practice2c([4, 3, 2, 4, 3, 6, 1, 5], True)))
#print("Prac 3b : %s" % chapter.practice3b())
print("Prac 6 : %s" % chapter.practice6(['green', 'blue', 'red']))

 