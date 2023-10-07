class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print("Name :",self.name)
        print("Id :",self.id)
s1=student("Harsh",371)
s1.display()
s2=student("Abhinav",252)
s2.display()