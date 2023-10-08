class Employee:
    def __init__(self,name,id):
        self.__name=name
        self.__id=id
    def __show(self):
        print(f"My name is {self.__name} & {self.__id}")
e1=Employee("Harsh", 371)
e1._Employee__show()