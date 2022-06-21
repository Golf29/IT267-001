from employee import Employee

class EmpMKT(Employee):
    def __init__(self,id,name,salary) -> None:
        super().__init__(id,name,salary)
        self.location = "Bangkok"
        self.commision = 30
        self.department = "Marketing"

    def add_location(self,location):
        self.location = location

    def add_commision(self,commisstion):
        self.commision = commisstion
    
    def emp_detail(self):
        print("==== Employee Marketing Detail =====")
        super().emp_detail()
        print(f'location: {self.location}')
        print(f'commision: {self.commision} year(s)')
    
    def mkt_salary(self):
        self._emp_salary()