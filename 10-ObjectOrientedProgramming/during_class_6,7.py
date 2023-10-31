class University:

    def __init__(self):
        # object attributes (object features)
        self.name = "CUE"

    # object methods (object behaviors)
    def print_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name


p1 = University()
p1.set_name("MIT")
p1.print_name()


