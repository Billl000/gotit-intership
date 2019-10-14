class Chapter:
    def __init__(self, name, total_exercise):
        self.name = name
        self.total_exercise = total_exercise

    def increase_exercise(self, n):
        self.total_exercise = self.total_exercise + n

    def print_ex(self):
        print(self.total_exercise)

    def print_name(self):
        print(self.name)