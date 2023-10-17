
#------------------------------------ Cash or Card -----------------------------------------------------#
while True:
    payment_method = input('Using Card or Cash?: ').lower().strip()
    if payment_method == "card" or payment_method == "cash":
        break
    else:
        print("Something went wrong! Please choose your payment method again.")
#------------------------------------------------Fare Cost-----------------------------------------------------#
while True:
    Fare_table =['phaya thai','ratchaprarop','makkasan','ramkhamhaeng','hua mak','ban thap chang','lat krabang','suvarnabhumi']
    origin = input('Where are you now?: ').lower().strip()
    destination = input('Where is your destination?: ').lower().strip()
    if origin != destination and origin in Fare_table and destination in Fare_table:
        distance_abs = abs(Fare_table.index(origin) - Fare_table.index(destination))
        cost = 0
        for i in range(1,distance_abs+1,1):
            if i == 1:
                cost +=15
            else:
                cost +=5
        break
    elif origin == destination:
        print("Origin and Destination can't be the same. Please type its again")
    elif origin not in Fare_table:
        print("Origin station doesn't exist in this Airport Rail Link line. Please type it again")
    elif destination not in Fare_table:
        print("Destination station doesn't exist in this Airport Rail link line. Please type it again")

#----------------------------------Member-----------------------------#
while True:
    amount_of_ticket = int(input('How many tickets?: '))
    if amount_of_ticket == int(amount_of_ticket) and amount_of_ticket >0:
        print(f'Your fare is {cost * amount_of_ticket} bath')        
        break
    elif amount_of_ticket <= 0:
        print("Ticket can't less than or equal to 0. Try again.")
    elif amount_of_ticket == str:
        print("Please type number.")
net_cost = amount_of_ticket * cost
#-------------------------------------pay method------------------------------------------#
#-----------cash-----------#
if payment_method == 'cash':
    while net_cost <0:
        customer_pay = int(input("Enter amount of money(1|5|10|20|50|100): "))
        net_cost -= customer_pay
    print(net_cost)






