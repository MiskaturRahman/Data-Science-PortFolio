class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

Miskatur = Employee()
Miskatur.salary = 100000
Miskatur.getSalary("Thanks!") # Employee.getSalary(Miskatur)
Miskatur.greet() # Employee.greet()
Miskatur.time()

