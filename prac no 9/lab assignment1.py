class Employee:
    def get_data(self):
        self.name = input("Name: ")
        self.age = int(input("Age: "))
        self.salary = float(input("Salary: "))
        self.address = input("Address: ")

    def show_data(self):
        print(self.name, self.age, self.salary, self.address)


class Manager(Employee):
    def get_manager(self):
        self.get_data()
        self.department = input("Department: ")

    def show_manager(self):
        self.show_data()
        print(self.department)


for i in range(2):
    m = Manager()
    m.get_manager()
    m.show_manager()