import time
class Animal:
    def __init__(self, type, name, date_brought = False, date_adopted = False): # initializes the parameters of instances of the Animal class, and it sets the date_brought and date_adopted as false as they will be inputted later
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

    def message(self, date_brought, date_adopted):        
        self.date_brought = date_brought
        self.date_adopted = date_adopted
        print(f"{self.name} was brought on {date_brought} and was adopted on {date_adopted}")

    

    


def Main():
    arrival_date = "september" #time.strftime("10/10/21") 
    zack = Animal("dog", "Zack", arrival_date)
    adoption_date = "october"
    # zack.setArrivalDate(arrival_date)
    # zack.setAdoptedDate(adoption_date)
    zack.message(arrival_date, adoption_date)



Main()