TICKET_PRICE =10
tickets_remaining = 100

# run this code over until tickets are  out
while tickets_remaining:

    # Output how many tickets remaining using the tickets_remaining variable

    print("There are {} tickets remaining".format(tickets_remaining))

    # Gather the users name and assign it to a new variable

    name = input("What is your name?  ")

    # prompt the user by name and ask how many tickets they would like

    tickets = input("Hey {} , How many tickets would you like?  ".format(name))
    tickets = int(tickets)
    # Calculate the price (number of tickets multiplied by cost) and assign to variable

    total_cost = TICKET_PRICE * tickets

    # Output the price to the screen

    print("Your tickets cost only {}".format(total_cost))

    # prompt user if they want to proceed Y/N

    proceed = input("Do you want to proceed? /n (Enter yes/no)")

    # if they want to proceed

    if proceed == "yes":
        # print sold to the screen
        print("SOLD!!")
        # and then decrement number of tickets from tickets purchased
        tickets_remaining -= tickets
    # otherwise....  thank them by name
    else:
        print("Thank you, {}!!".format(name))

# notify user tickets are sold out

print("Tickets are sold out!!")