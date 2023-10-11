class superclass:
  def super_method(self):
    print("Super Class Method Call")
class DerviedClass1(superclass):
  def dervied1_method(self):
    print("Dervied Class 1 Method Call")
class DerviedClass2(DerviedClass1):
  def dervied2_method(self):
    print("Dervied Class 2 Method Call")
obj = DerviedClass2()
obj.super_method()
obj.dervied1_method()
obj.dervied2_method()