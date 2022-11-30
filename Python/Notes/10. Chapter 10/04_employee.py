class Employee:
    company = "Google"
    salary = 100

Miskatur = Employee()
rajni = Employee()
Miskatur.salary = 300
rajni.salary = 400

print(Miskatur.company)
print(rajni.company)
Employee.company = "YouTube"
print(Miskatur.company)
print(rajni.company)
print(Miskatur.salary)
print(rajni.salary)