class Cart:
    
    def __init__(self):
        
        self.cart = {}
        self.item_list = { 
                'egg':2.99, 
                'milk': 3.99, 
                'bread': 5.99, 
                'cereal': 9.99, 
                'meat': 10.99
                }

    
    def show(self):
        if len(self.cart) != 0:
            print('Items in your cart: ')
            for name, price in self.cart.items():
                print('{}: {}'.format(name, price))

        else:
            print('Your cart is empty')

    def add(self):
        print('\nMenu')
        print('\n'.join(['{}-${}'.format(name, price) for name, price in self.item_list.items()]))
        name = input()

        if name in self.item_list:
            self.cart[name] = self.item_list[name]
            print('Item added. Thank you.')

        else:
            print('Invalid item. Please try again')

    def delete(self):
        if len(self.cart) != 0:
            print('Choose the item to delete from your cart: ')
            for name, price in self.cart.items():
                print('{}: {}'.format(name, price))

            name = input()
            if name in self.cart:
                del self.cart[name]
                print('Item deleted.')

            else:
                print('Item not present in cart.')

        else:
            print('Your cart is empty')

    def total(self):
        return sum(self.cart.values())

    # return length of cart
    def length(self):
        return len(self.cart)

def main():
    cart = Cart()

    # while loop for repeated menu
    while True:
        
        print('\nShow\nAdd\nDelete\nQuit? ')
        choice = input()
        if choice.lower() == 'show':
            cart.show()

        elif choice.lower() == 'add':
            cart.add()

        elif choice.lower() == 'delete':
            cart.delete()

        elif choice.lower() == 'quit':
            if cart.length() != 0:
                cart.show()
                print('Your total is: ', cart.total())
                print('Pay up or else....')
                break

            else:
                print('Your cart is empty')
                break
        
        else:
            print('Incorrect response, try again')

main()