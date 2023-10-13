class employee:
    companyname = "Amazon"
    def show(self):
        print(f"I am {self.name} My company is {self.companyname}")
    @classmethod
    def changename(self,newcompany):
        self.companyname=newcompany
e1=employee()
e1.name="Harsh"
e1.show()
e1.changename("Innovaccer")
e1.show()