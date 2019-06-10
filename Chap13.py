class chap13:
    def practice1(self, array, value):
        i = len(array) - 1
        while i != -1 and array[i] != value:
            i = i - 1

            if i == -1:
                return -1
            else:
                return i

        for i in range(len(array) - 1, -1, -1):
            if array[i] == value:
                return i
            return -1

    def practice4SSort(self, array):
        i = 0
        j = 1
        while i != len(array):
            if array[i] < array[j]:
                j = array[i]
            array[i], array[j] = array[j], array[i]
            i = i + 1

        return array

    def practice4ISort(self, array):
        i = 0
        while i != len(array):
            j = i
            while j != 0 and array[j - 1] >= array[i]:
                j = j - 1
            value = array[i]
            del array[i]
            array.insert(j, value)
            i = i + 1

        return array

    def practice5b(self, lst):
        while end > 0:
            for i in range(0, end):
                if lst[i] > lst[i + 1]:
                    tmp = lst[i + 1]
                    lst[i + 1] = lst[i]
                    lst[i] = tmp
            end = end - 1



chap13().practice4SSort([6, 5, 4, 3, 7, 1, 2])
