class RUPP:
    def __inint__(self, name):
        self.name = name
    def getFacilityName(self):
        print(f'welcome to RUPP from facility {self.name}')

#creating instance 
obj = RUPP()
obj.name = "engineering"
obj.getFacilityName()