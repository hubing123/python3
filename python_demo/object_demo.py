# class myclas:
#     def _init_(self):
#         print("this is my class")
# obj=myclas()
class myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj1=myclass("hubing",14)
obj2=myclass("william",22)
print(obj1.name)
print(obj1.age)
print(obj2.name)
print(obj2.age)