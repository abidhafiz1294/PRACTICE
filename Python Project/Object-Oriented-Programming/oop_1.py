class Person:
  #CLASS Variable
  no_of_person= 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Person.no_of_person += 1

  @classmethod
  def set_reset_age(cls,name,age):
    cls.name = name
    cls.age = age
    return cls

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36) ## perallal concept
print(p1.age)

p2 = Person("Arham", 78)
print(p2.no_of_person)

p3= Person.set_reset_age("Johan", 56)
print(p3.name)

Person.myfunc(Person("John", 36))

print(Person.no_of_person)
