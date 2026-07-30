class Employee : 
    company_name = "PREM Corp"


    def __init__(self,employee_id,name):
        self.employee_id = employee_id
        self.name = name

    def work(self):
        return (f'{self.name} is (ID : {self.employee_id}) is working !!')

    def get_info(self):
        return (f"{self.name} - {self.employee_id}-{self.company_name}")

## Object Creation 

employee1 = Employee("Code-1","Om")
employee2 = Employee("Code-2","Rahul")

print(employee1.work())
print(employee2.get_info())

        