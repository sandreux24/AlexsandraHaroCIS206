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


employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")


employee1.displayEmployeeInfo()
employee2.displayEmployeeInfo()
employee3.displayEmployeeInfo()



