from random import randint
class Train():

    def __init__(self,trn):
        self.trn = trn

    def book(self,f,t):
        print(f"Your ticket is Successfully booked in train no.{self.trn} from {f} to {t}")

    def status(self):
        print(f"Your Ticket has confirmed for train_no.{self.trn}")

    def fare(self):
        print(f"Your ticket fare of train_no.{self.trn} is {randint(200,300)}")

n = randint(3468,65528)
a =  Train(n)

a.book("HYD","DEl")
a.fare()
a.status()