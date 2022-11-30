class Employee:
    company = "Google"
    salary = 100

Miskatur = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# Miskatur.salary = 300
# rajni.salary = 400
Miskatur.salary = 45
print(Miskatur.salary)
print(rajni.salary)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 