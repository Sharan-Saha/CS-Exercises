import time
class Animal:
    def __init__(self, type, name, date_brought, date_adopted = False):
        self.name = name
        self.type = type 
        self.id = id(self)
        self.date_brought = date_brought
        self.date_adopted = date_adopted

    def setArrivalDate(self, date_brought):
        self.date_brought = date_brought
        print(f"{self.name} was brought on {date_brought}")

    def setAdoptedDate(self, date_adopted):
        self.date_adopted = date_adopted
        print(f"{self.name} was adopted on {date_adopted}")

    

    


def Main():
    arrival_date = time.strftime("10/10/21")
    zack = Animal("dog", "Zack", arrival_date)
    adoption_date = time.strftime("10/18/21")
    zack.setArrivalDate(arrival_date)
    zack.setAdoptedDate(adoption_date)



Main()