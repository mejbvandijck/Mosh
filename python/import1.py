class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age  = age
    
    def fullname(self):
        full = [self.firstname, self.lastname]
        return ' '.join(full)
    
    def __str__(self):
        return self.firstname