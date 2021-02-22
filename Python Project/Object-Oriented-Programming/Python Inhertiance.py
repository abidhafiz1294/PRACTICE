class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname,self.age)

class Student(Person):
  def __init__(self, fname, lname,age):
      Person.__init__(self,fname,lname)
      self.age= age

x = Student("Mike", "Olsen",56)
x.printname()
print(help(Person))
print(help(Student))
