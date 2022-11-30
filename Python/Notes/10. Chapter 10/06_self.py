class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

Miskatur = Employee()
Miskatur.salary = 100000
Miskatur.getSalary() # Employee.getSalary(Miskatur)