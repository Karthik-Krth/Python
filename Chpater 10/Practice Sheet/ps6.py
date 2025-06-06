from random import randint
class Train():

    def __init__(kr,trn):
        kr.trn = trn

    def book(kr,f,t):
        print(f"Your ticket is Successfully booked in train no.{kr.trn} from {f} to {t}")

    def status(kr):
        print(f"Your Ticket has confirmed for train_no.{kr.trn}")

    def fare(kr):
        print(f"Your ticket fare of train_no.{kr.trn} is {randint(200,300)}")

n = randint(3468,65528)
a =  Train(n)

a.book("HYD","DEl")
a.fare()
a.status()