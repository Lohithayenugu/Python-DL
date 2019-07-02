class Person:
    __per_count=0
    def _init_(self,name,age,family):
        self.__name=name
        self.__age=age
        self.__family=family
        Person._per_count=Person._per_count+1

    @classmethod
    def get_persons_count(self):
        return  Person.__per_count

    def get_name(self):
        return self.__name

    def get_family(self):
        return self.__family
    def get_age(self):
        return self.__age



class Employee (Person):
    __emp_count = 0
    __avg_sal = 0.0

    def _init_(self, name, age, family, department,salary,EID):
        self.__salary=salary
        self.__department=department
        self.__EID=EID
        Employee._emp_count=Employee._emp_count+1
        Employee._avg_sal=Employee._avg_sal+salary
        Person._init_(self,name,age,family)

    @classmethod
    def average_salary(self):
        if Employee.__emp_count>0:
            return Employee._avg_sal / Employee._emp_count
        else:
            return 0

    @classmethod
    def get_employees_count(self):
        return Employee.__emp_count

    def get_department(self):
        return self.__department

    def get_salary(self):
        return self.__salary
    def get_EID(self):
        return self.__EID

class Passenger (Person):
    __pas_count = 0

    def _init_(self, name, age, family, PID):
        Passenger._pas_count=Passenger._pas_count+1
        Person._init_(self,name,age,family)
        self.__PID=PID

    def get_PID(self):
        return self.__PID

    @classmethod
    def get_passengers_count(self):
        return Passenger.__pas_count

class Flight :
    __flights_count = 0

    def _init_(self,name, FID, seats_count):
        Flight._flights_count=Flight._flights_count+1
        self.__FID=FID
        self.__fname=name
        self.__seats_count=seats_count
        self.__passengers={}
        self.__available_seats_count=seats_count

    def get_FID(self):
        return self.__FID
    def get_seats_count(self):
        return self.__seats_count
    def get_available_seats_count(self):
        return self.__available_seats_count
    def get_fname(self):
        return self.__fname
    @classmethod
    def get_flights_count(self):
        return Flight.__flights_count

    def assign_passenger(self,p,pid):
        if(self.__available_seats_count>0):
            self.__passengers[pid]=p
            self._available_seats_count=self._available_seats_count-1
            print('Passenger added')
        else:
            print('No seats available')
    def remove_passengers(self,p,pid):
        if(pid in self.__passengers):
            #self.__passengers.remove(p)
            self.__passengers.pop(pid)
            self._available_seats_count=self._available_seats_count+1
            print('Passenger removed')
        else:
            print('No Passenger')

    def get_passengers_list(self):
        return self.__passengers
print("Select from below")
print("Case 1 :Create Employee class object\nCase 2 :Create Passenger class object\nCase 3 :Create Flight class object\n 4 :View average salary of Emplyees\n"
      +"Case 5 :View Flights count\nCase 6 :View Employees count\nCase 7 :View Passengers count\nCase 8 :View Employee Deails\nCase 9 :View Flight Details\nCase 10 :View Passengers Details\n"
       "Case 11 :View Flight Passengers\nCase 12 :Add Passenger\n Case 13 :Remove Passenger\nCase 14 :Exit")

bool=1
employees_list={}
passengers_list={}
flights_list={}
def addEmployee():
    name=str(input("Enter name"))

    EID = str(input("Enter EID"))

    j = 1
    while (j):
        try:
            age = int(input("Enter age"))
            j = 0
        except ValueError:
            print('Non-numeric data.')
    j = 1
    while(j):
        try:
            salary=float(input("Enter salary"))
            j=0
        except ValueError:
            print('Non-numeric data.')
    department=str(input("Enter department"))
    family=str(input("Enter family"))
    E1=Employee(name,age,family,department,salary,EID)
    employees_list[EID]=E1
    print("Employee added")

def addPassenger():
    name=str(input("Enter name"))
    j = 1
    while(j):
        try:
            age=int(input("Enter age"))
            j=0
        except ValueError:
            print("Non-numeric data")

    pid = str(input("Enter PID"))


    family=str(input("Enter family"))
    P1=Passenger(name,age,family,pid)
    passengers_list[pid]=P1
    print("Passenger added")
def addFlight():
    name=str(input("Enter name"))

    fid=str(input("Enter fid"))

    j = 1
    while (j):
        try:
            seats_count = int(input("Enter seats count"))
            j = 0
        except ValueError:
            print("Non-numeric data")
    F1=Flight(name,fid,seats_count)
    flights_list[fid]=F1
    print("Flight added")
def EmployeeAvgSal():
    print("Employee Average Salary: "+str(Employee.average_salary()))

def EmpCount():
    print("Employee Count: " + str(Employee.get_employees_count()))
def FlightsCount():
    print("Flights Count: " + str(Flight.get_flights_count()))

def passengerCount():
    print("Passenger Count: " + str(Passenger.get_passengers_count()))
def ViewEmployee():
    if(len(employees_list)>0):
        for key in employees_list:
            print(str(key))
        name=str(input("Select Employee"))
        if(name in employees_list):
            print("Name : "+employees_list[name].get_name()+"\nSalary :"+str(employees_list[name].get_salary())+"\n Department : "+employees_list[name].get_department()+"\n Family : "+employees_list[name].get_family()+"\n Age : "+str(employees_list[name].get_age())+"\n EID : "+name)
        else:
            print("invalid employee ID")
    else:
        print("No employees to view")
def ViewPassenger():
    if(len(passengers_list)>0):
        for key in passengers_list:
            print(str(key))
        name=str(input("Select Passenger"))
        if(name in passengers_list):
            print("Name : "+passengers_list[name].get_name()+"\n Age : "+str(passengers_list[name].get_age())+"\n Family : "+passengers_list[name].get_family()+"\n PID : "+name)
        else:
            print("invalid passenger ID")
    else:
        print("No passengers to view")
def ViewFlight():
    if(len(flights_list)>0):
        for key in flights_list:
            print(str(key))
        name=str(input("Select Flight"))
        if(name in flights_list):
            print("Name : "+flights_list[name].get_fname()+"\n Seats Count : "+str(flights_list[name].get_seats_count())+"\n Available Seats Count : "+str(flights_list[name].get_available_seats_count())+"\n FID : "+name)
        else:
            print("invalid flight ID")
    else:
        print("No flights to view")
def AddPassenger():
    if(len(flights_list)>0):
        for key in flights_list:
            print(str(key))
        name=str(input("Select Flight"))
        if(name in flights_list):
            print('Selected Flight : '+flights_list[name].get_fname())
            if(len(passengers_list)>0):
                for key in passengers_list:
                    print(str(key))
                pname = str(input("Select Passenger"))
                if (pname in passengers_list):
                    print('Selected passenger : ' + passengers_list[pname].get_name())
                    if(pname not in flights_list[name].get_passengers_list()):
                        flights_list[name].assign_passenger(passengers_list[pname],pname)
                    else:
                        print('Passenger already in flight')
                else:
                    print("Invalid Passenger")
            else:
                print('No Passengers to add')
        else:
            print("invalid flight ID")
    else:
        print("No flights available")
def RemovePassenger():
    if(len(flights_list)>0):
        for key in flights_list:
            print(str(key))
        name=str(input("Select Flight"))
        if(name in flights_list):
            print('Selected Flight : '+flights_list[name].get_fname())
            if(len(flights_list[name].get_passengers_list())>0):
                for key in flights_list[name].get_passengers_list():
                    print(key)
                pname = str(input("Select Passenger"))
                if (pname in flights_list[name].get_passengers_list()):
                    flights_list[name].remove_passengers(passengers_list[pname],pname)
                else:
                    print("Invalid Passenger")
            else:
                print('No Passengers to remove')
        else:
            print("invalid flight ID")
    else:
        print("No flights available")
def ViewFlightPassengers():
    if (len(flights_list) > 0):
        for key in flights_list:
            print(str(key))
        name = str(input("Select Flight"))
        if (name in flights_list):
            for i in flights_list[name].get_passengers_list():
                print(i)
        else:
            print("invalid flight ID")
    else:
        print("No flights available")

def Exit():
    global bool
    bool=0
def choices(argument):
    switcher = {
        1:  addEmployee,
        2:  addPassenger,
        3:  addFlight,
        4:  EmployeeAvgSal,
        5:  FlightsCount,
        6:  EmpCount,
        7:  passengerCount,
        8:  ViewEmployee,
        9:  ViewFlight,
        10: ViewPassenger,
        11: ViewFlightPassengers,
        12: AddPassenger,
        13: RemovePassenger,
        14: Exit
    }
    # Get the function from switcher dictionary
    func = switcher.get(int(argument), lambda: "Invalid choice")
    func()
while(bool!=0):
    choice =input("Enter your choice")
    choices(choice)
