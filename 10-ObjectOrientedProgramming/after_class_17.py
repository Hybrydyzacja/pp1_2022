class Statisctics():
    def __init__(self, numbers_set):
        self.numbers_set = numbers_set
        self.greatest_number = []
        self.smallest_number = []
        self.mean_numbers = []

    def greatest(self, numbers_set):
        self.greatest_number = max(numbers)

    def smallest(self):
        self.smallest_number = min(self.numbers_set)

    def mean(self):
        self.mean_numbers = sum(self.numbers_set)/len(self.numbers_set)

    def show_status(self):
        print(self.numbers_set)
        print(self.greatest_number)
        print(self.smallest_number)
        print(self.mean_numbers)


numbers = Statisctics([12, 37, 6, 9, 17])

numbers.show_status()

# numbers = [12, 37, 6, 9, 17]
# x = min(numbers)
# y = max(numbers)
# z = sum(numbers)/len(numbers)
# print(x, y, z)