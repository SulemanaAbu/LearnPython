class Student:
    def __init__(self, student_name, student_number, program, year):
        self.student_name = student_name
        self.student_number = student_number
        self.program = program
        self.year = year

    def study(self):
        print(f"{self.student_name} {self.student_number} studied {self.program} in {self.year}")

    def defer(self):
        print(f"{self.student_name} {self.student_number} deferred {self.program} in {self.year}")
