from django.test import TestCase

# Create your tests here.
class emp:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name +" "+ str(self.age)


e1= emp("ram",70)

print(e1)

