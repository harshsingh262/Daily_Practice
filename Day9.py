class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class programmer(employee):
    def __init__(self,name,id,language):
        super().__init__(name,id)
        self.language=language
p1=programmer("Harsh",371,"Python")
print(p1.name)