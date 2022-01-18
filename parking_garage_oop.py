available_space = { 
        1:"slot",
        2:"slot",
        3:"slot",
        4:"slot",
        5:"slot",
        6:"slot",
        7:"slot",
        8:"slot",
        9:"slot",
        10:"slot"
        
}

parking_garage = {} 



class Parking():
    

    def show_spaces(self):
        
        print("Parking Spaces Left:")
        if available_space:
            print(len(available_space))
            
        else:
            print("Sorry! No Parking Spaces Available.")
        

    def take_ticket(self):
        
       
        ticket = list(available_space)[0]
        parking_garage.update({ticket:available_space[ticket]})        
        del available_space[ticket]
        print(f'Your ticket is #{ticket}')
        
    def pay_ticket(self):
        
        while True:
            ticket_number_response = int(input("What is your ticket #?\n '0' to quit\n "))
            if ticket_number_response == 0:
                break
            elif ticket_number_response in parking_garage.keys():
                confirm = input(f'Your ticket # is {ticket_number_response} is that correct? Y/N ')
                while True:
                    if confirm.lower() == 'y':
                        payment = input('Your total is $10\nDebit or Credit  or cash?\n')
                        if payment.lower() == 'debit' or payment.lower() == 'credit' or payment.lower() == 'cash':
                            parking_garage[ticket_number_response] = 'Paid'
                            print("Thank you for your payment YOU MAY LEAVE NOW\n")
                            break
                    elif confirm.lower() == 'n':
                        break
                    else:
                        print("Invalid Response, Try Again")
            else:
                print("Invalid Response, Try Again")


    def leave_garage(self):
      
        
        while True:
            show_ticket = int(input("Type '0' to quit\nShow your ticket number: "))
            if show_ticket == 0: 
                break
            elif parking_garage.get(show_ticket) == 'Paid':
                print("Thank you for Parking!")
                parking_garage[show_ticket] = "unpaid"
                available_space.update({int(show_ticket):parking_garage[show_ticket]})
                
                del parking_garage[show_ticket]
                break
            elif parking_garage.get(show_ticket) == 'slot':
                print("Please pay your ticket before leaving")
                
                
            else:
                print("Invalid Response, Try Again")
                

    
    def user(self):
        while True:
            response = input("What would you like to do?\n 'Show Spaces'/'Take Ticket'/'Pay Ticket'/'leave'/'Quit'\n")
            if response.lower() == 'quit':
                print("Please visit us again!")
                break
            elif response.lower() == 'show spaces':
                self.show_spaces()
            elif response.lower() == 'take ticket':
                self.take_ticket()
            elif response.lower() == 'pay ticket':
                self.pay_ticket()
            elif response.lower() == 'leave':
                self.leave_garage()
            else:
                print("Invalid Response, Try Again")

        



run = Parking()
run.user()      