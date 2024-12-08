class Employee:
    def __init__(self, name, idNumber, department, position):
        self.name = name
        self.idNumber = idNumber 
        self.department = department
        self.position = position

    def __init__(self, name="", idNumber=0, department="", position=""):
        self.name = name
        self.idNumber = idNumber 
        self.department = department
        self.position = position

    def getName(self):
        return self.name
    
    def getidNumber(self):
        return self.idNumber
    
    def getDepartment(self):
        return self.department
    
    def getPosition(self):
        return self.position
    
    
    def setName(self, name):
        self.name = name
    
    def setidNumber(self, idNumber):
        self.idNumber = idNumber
    
    def setDepartment(self, department):
        self.department = department
    
    def setPosition(self, position):
        self.position = position


    def displayEmployeeInfo(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.idNumber}")
        print(f"Department: {self.department}")
        print(f"Position: {self.position}")
        print()




    def calculateSalary(self, hoursWorked, ratePerHour=None):
        if ratePerHour is None:
            salary = hoursWorked * 20
        else:
            salary = hoursWorked *ratePerHour

        print(f"Salary: {salary}")


    def work(self):
        print(f"{self.name} is working as a {self.position}.")

class Manager(Employee):
    def __init__(self, name, idNumber, department, position, bonus):
        super().__init__(name, idNumber, department, position)
        self.bonus = bonus

    def displayEmployeeInfo(self):
        super().displayEmployeeInfo()
        print(f"Bonus: {self.bonus}")

    def work(self):
        print(f"{self.name} is managing the {self.department} department as a {self.position}.")

        





employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
manager1 = Manager("James Bond", 10001, "IT", "IT Manager", 5000)

employees = [employee1, employee2, employee3, manager1]

for emp in employees:
    emp.work()

employee1.calculateSalary(40)  
employee2.calculateSalary(40, 30)

employee1.displayEmployeeInfo()
employee2.displayEmployeeInfo()
employee3.displayEmployeeInfo()
manager1.displayEmployeeInfo()
