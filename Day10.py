class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"This is name {self.name}")
class dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"This is Dance {self.dance}")
class employeedancer(employee, dancer):
    def __init__(self, name,dance):
        self.name=name
        self.dance=dance
obj=employeedancer("Harsh","HipHop")
print(obj.name)
obj.show()
        