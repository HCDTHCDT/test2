class Employee:
    def __init__(self,first,last,pay):
        #a convection .... self is default..
        self.first=first
        #not necessarily same ... self.firstname=first is also OK
        self.last=last
        self.pay=pay
        #self.mail=first +"."+last+"@company.com"
    @property
    def mail(self):
        return ("{}.{}@email.com".format(self.first, self.last))
    @property
    def fullname(self):
        return ("{} {}".format(self.first, self.last))
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        self.first=first
        self.last=last
    @fullname.deleter
    def fullname(self):
        print("Deleted !")
        self.first=None
        self.last=None

emp_1=Employee("Hasi","Hasavi",40000)

emp_1.first="Kakiii"

print(emp_1.first)
print(emp_1.mail)#wrong for methods
print(emp_1.fullname)#() without property
#what is the problem?...email has been set once at the beginning...we can create a method for that like fullname()
#or use set & get
#in order to access mail like an attribute we should add a property decorator to the method
#print(emp_1.mail())
# now it has type error
#try to set them again
#emp_1.mail="gggggggg"
#ERROR
#now use setter & getter
emp_1.fullname="Ali Alavi"
print(emp_1.fullname)
#delete
del emp_1.fullname
print(emp_1.fullname)
