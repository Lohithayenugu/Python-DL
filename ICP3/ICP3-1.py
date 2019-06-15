class Employee:
    __emp_count=0
    _sal=0.0
    def __init__(self,name,salary,family,department):
        self.__name=name
        self.__salary=salary
        self.__family=family
        self.__department=department
        Employee.__emp_count=Employee.__emp_count+1
        Employee._sal=Employee._sal+salary
    @classmethod
    def average_salary(self):
        if Employee.__emp_count>0:
            return Employee._sal/Employee.__emp_count
        else:
            return 0

    @classmethod
    def get_employees_count(self):
        return  Employee.__emp_count

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_family(self):
        return self.__family

    def get_department(self):
        return self.__department

class FulltimeEmployee (Employee):
    __emp_count = 0
    _sal = 0.0

    def __init__(self, name, salary, family, department):
        FulltimeEmployee.__emp_count=FulltimeEmployee.__emp_count+1
        FulltimeEmployee._sal=FulltimeEmployee._sal+salary
        super().__init__(name,salary,family,department)
    @classmethod
    def average_salary(self):
        if FulltimeEmployee.__emp_count>0:
            return FulltimeEmployee._sal / FulltimeEmployee.__emp_count
        else:
            return 0

    @classmethod
    def get_employees_count(self):
        return FulltimeEmployee.__emp_count



print("Select from below")
print("Case 1 :Create Employee class object\nCase 2 :Create Fulltime Employee class object\nCase 3 :View average salary of Emplyees\n"
      +"Case 4 :View average salary of Full time employees\nCase 5 :View Employees count\nCase 6 :View full-time employees count\nCase 7 :View Employee Deails\nCase 8 :View Full-Time Employee Details\nCase 9 :Exit")

bool=1
employee={}
ftEmployee={}
def addEmployee():
    name=str(input("Enter name"))
    j = 1
    while(j):
        try:
            salary=float(input("Enter salary"))
            j=0
        except ValueError:
            print('Non-numeric data.')
    department=str(input("Enter department"))
    family=str(input("Enter family"))
    E1=Employee(name,salary,family,department)
    employee[name]=E1
    print("Employee added")

def addFullTimeEmployee():
    name=str(input("Enter name"))
    j = 1
    while(j):
        try:
            salary=float(input("Enter salary"))
            j=0
        except ValueError:
            print("Non-numeric data")
    department=str(input("Enter department"))
    family=str(input("Enter family"))
    F1=FulltimeEmployee(name,salary,family,department)
    ftEmployee[name]=F1
    print("Full-Time Employee added")
def EmployeeAvgSal():
    print("Employee Average Salary: "+str(Employee.average_salary()))
def FTEmpAvgSal():
    print("Full-Time Employee Average Salary:"+str(FulltimeEmployee.average_salary()))

def EmpCount():
    print("Employee Count: " + str(Employee.get_employees_count()))

def FTEmpCount():
    print("Full-Time Employee Count: " + str(FulltimeEmployee.get_employees_count()))
def ViewEmployee():
    if(len(employee)>0):
        for key in employee:
            print(str(key))
        name=str(input("Select Employee"))
        if(name in employee):
            print(employee[name].get_name()+" "+str(employee[name].get_salary())+" "+employee[name].get_department()+" "+employee[name].get_family())
        else:
            print("invalid name")
    else:
        print("No employees to view")
def ViewFTEmployee():
    if (len(ftEmployee) > 0):
        for key in ftEmployee:
            print(str(key))
        name=str(input("Select Full-Time Employee"))
        if (name in ftEmployee):
            print(ftEmployee[name].get_name()+" "+str(ftEmployee[name].get_salary())+" "+ftEmployee[name].get_department()+" "+ftEmployee[name].get_family())
        else:
            print("invalid name")
    else:
        print("No full-time employees to view")

def Exit():
    global bool
    bool=0
def choices(argument):
    switcher = {
        1:  addEmployee,
        2:  addFullTimeEmployee,
        3:  EmployeeAvgSal,
        4:  FTEmpAvgSal,
        5:  EmpCount,
        6:  FTEmpCount,
        7:  ViewEmployee,
        8:  ViewFTEmployee,
        9:  Exit
    }
    # Get the function from switcher dictionary
    func = switcher.get(int(argument), lambda: "Invalid choice")
    func()
while(bool!=0):
    choice =input("Enter your choice")
    choices(choice)

