class Employee:
    def __init__(self, first_name, last_name, salary=5000):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self):
        self.salary += 50000
    def employee_info(self):
        full_name = self.first_name + ' ' + self.last_name
        print(full_name.title())