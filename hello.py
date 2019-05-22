class chap3:
    def practice1():
        int a = min(2, 3, 4);
        int b = max(2, -3, 4, 7, -5);
        int c = max(2, -3, min(4, 7), -5);
        print(a + ", " + b + ", " + c);

    def practice2():
        int a = min(max(3, 4), abs(-5));
        int b = abs(min(4, 6, max(2, 8)));
        int c = round(max(5.572, 3.258), abs(-2));
        print(a + ", " + b + ", " + c);

    def practice3(self, index1):
        return index1 * 3;

    def practice4(self, index1, index2):
        return abs(index2 - index1);

    def practice5(self, index1):
        return index1 / 5 * 8;

    def practice6(self, index1, index2, index3):
        return mean(index1 + index2 + index3, 3);

    def practice7(self, index1, index2, index3, index4):
        int sum = sum(index1, index2, index3, index4);
        int Max_Total = sum - min(index1, index2, index3, index4);
        return Max_Total / 3;


    def practice8(day1, day2):
        return int(abs(day2 - day1) / 7);

    def practice9and10(num):
        return pow(num, 2);








