class BaseInfo:
    def __init__(self,name,eid,age):
        self.name = name
        self.eid = eid
        self.age = age
    def showdetails(self):
        print(self.__dict__)

class Teacher(BaseInfo):
        def showdetails(self):
            super().showdetails()
            print('Abey jaa naa..')

obj = Teacher('SRB',1,21)
obj.showdetails()
setattr(obj,'name','Sourabh')
obj.showdetails()
