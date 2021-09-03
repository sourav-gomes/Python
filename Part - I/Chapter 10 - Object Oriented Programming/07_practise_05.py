import random
import collections

class Train:
    global s1
    s1 = set()
    # global s
    
    def __init__(self, tname, fare, seats):
        self.name = tname
        self.fare = fare
        self.seats = seats
        for i in range(self.seats):
            s1.add(i+1)
        print(f"List just after instantiation is: {s1}")
    
    def getStatus(self):
        print("***************")
        print(f"The name of the train is: {self.name}")
        print(f"The seats available are: {self.seats}")
        print("***************")

    def fareInfo(self):
        print(f"The price of {self.name} ticket is Rs. {self.fare}")

   
    def bookTickets(self):
        s = self.seats 
        print(s)
        randNo = random.randint(1, s)
        print(randNo)
        if (s > 0):
            s1.remove(randNo)
            print(f"Your ticket has been booked! Your seat no. is {randNo}")
            s -= 1
            self.seats = self.seats - 1
            print(s1)
        else:
            print(f"Sorry, currently there are no seats available. Try Tatkal.")
    
    # @staticmethod
    def cancelTicket(self, seatNo):
        if seatNo in s1:
            j = True
        else:
            s1.add(seatNo)
            j = False
                    
        if (j):
            print(f"Sorry, this is an invalid Seat number.Try again.")

        else:
            print(f"Your ticket is cancelled. Refund in process...")
            self.seats = self.seats + 1
            print(s1)            
            

intercity = Train('Rajdhani', 100, 5)

intercity.getStatus()

intercity.fareInfo()

intercity.bookTickets()

intercity.bookTickets()

intercity.bookTickets()

intercity.cancelTicket(3)

intercity.cancelTicket(1)


