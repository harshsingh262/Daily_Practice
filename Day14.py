class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def frmstring(cls,string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
e1=employee("Harsh",100000)
print(e1.name)
print(e1.salary)
string="shinu-100000"
e2=employee.frmstring(string)
print(e2.name)
print(e2.salary)
