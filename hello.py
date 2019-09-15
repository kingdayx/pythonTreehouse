SERVICE_CHARGE = 2
TICKET_PRICE =10
tickets_remaining = 100

# create calculate_price function. It takes tickets and returns TICKET_PRICE * tickets

def calculate_price(number_of_tickets):
    # add the service charge to our result
    return TICKET_PRICE * number_of_tickets + SERVICE_CHARGE

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
        total_cost = calculate_price(tickets)
        print("Your tickets cost only {}".format(total_cost))
        proceed = input("Do you want to proceed? /n (Enter yes/no)")
        if proceed == "yes":
            # To do: gather credit card info and process it
            print("SOLD!!")
            tickets_remaining -= tickets
        else:
            print("Thank you, {}!!".format(name))
print("Tickets are sold out!!")