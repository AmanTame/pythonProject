class Car:
    def __init__(self,mk,md,yr,cl):
        self.make = mk
        self.model = md
        self.year = yr
        self.color = cl
    def drive(self):
        print("This "+self.model+" is driving!")
    def stop(self):
        print("This "+self.model+" is stopped!")


