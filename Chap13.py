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
        x = 0
        while i != len(array):
            if array[i] < array[j]:
                j = array[i]
                x = array[i]
                array[i]= array[j]
                array[j] = x
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
        end = len(lst) - 1
        while end > 0:
            for i in range(0, end):
                if lst[i] > lst[i + 1]:
                    tmp = lst[i + 1]
                    lst[i + 1] = lst[i]
                    lst[i] = tmp
            end = end - 1


chap = chap13()
print("Prac 1 : %s" % chap.practice1([4, 5, 2, 5], 5))
print("Prac 4S : %s" % chap.practice4SSort([5, 6, 2, 6, 8, 3]))
print("Prac 4T : %s" % chap.practice4ISort([5, 6, 2, 6, 8, 3]))
print("Prac 5b : %s" % chap.practice5b([6, 2, 4, 3]))
