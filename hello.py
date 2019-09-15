TICKET_PRICE =10
tickets_remaining = 100

while tickets_remaining:
    print("There are {} tickets remaining".format(tickets_remaining))
    name = input("What is your name?  ")
    tickets = input("Hey {} , How many tickets would you like?  ".format(name))
    try:
        tickets = int(tickets)
        if tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("oh no! we ran into an issue. {} please try again".format(err))
    else:
        total_cost = TICKET_PRICE * tickets
        print("Your tickets cost only {}".format(total_cost))
        proceed = input("Do you want to proceed? /n (Enter yes/no)")
        if proceed == "yes":
            print("SOLD!!")
            tickets_remaining -= tickets
        else:
            print("Thank you, {}!!".format(name))
print("Tickets are sold out!!")