class product:
    '''Class product contains the id, quantity, and price of a given product'''
    def __init__(self, name, id, quantity, price):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.price = price
    def addproduct(self,ammount):
        self.quantity = self.quantity + ammount
    def sellproduct(self,ammount):
        self.quantity = self.quantity - ammount
    def __str__(self):
        return f'{self.name} (id {self.id}) has a price of ${self.price}. There are {self.quantity} in stock.'

class store_inventory:
    def __init__(self,store_name):
        self.store_name = store_name
        self.items = []
    def add_item(self,item):
        self.items.append(item)
    # def inventory_value(self):
    #     total = 0
    #     for i in self.items:
    #         total += (i.price*i.quantity)
    #     return f'{total}$ worth of inventory in stock'
    # def total_inventory (self):
    #     for i in self.items:
    #         print(f'{i.name} quantity: {i.quantity} price: {i.price}')
    def __str__(self):
        return self.store_name

def make_a_sale():
    item_to_adjust = ''
    while item_to_adjust not in inventory_dict:
        item_to_adjust = input('Which item are you selling? ')
    ammount_sold = ''
    while type(ammount_sold) != int:
        try:
            ammount_sold = int(input('How many units have been purchased? '))
        except ValueError:
            continue
    inventory_dict[item_to_adjust].sellproduct(ammount_sold)
#    print(inventory_dict[item_to_adjust])

def new_item(store_name):
    item_name = input('What is the item name? ')
    item_no = input('What is the item No? ')
    item_quantity = int(input('What is the starting inventory? '))
    item_price = float(input('How much are we selling them for? '))
    item = product(item_name, item_no, (item_quantity), (item_price))
    store_inventory(store_name).add_item(item)
    inventory_dict[item_name] = item
#    print(inventory_dict)

def update_inventory():
    item_name = ''
    while item_name not in inventory_dict:
        item_name = input('What item would you like to update? ')
    ammount_added = ''
    while type(ammount_added) != int:
        try:
            ammount_added = int(input('How many units have been added? '))
        except ValueError:
            continue
    inventory_dict[item_name].addproduct(ammount_added)
#    print(inventory_dict[item_name])

#initilize the store with two items and create dictionary to store items in for lookup

toilet_paper = product('toilet paper',1,10,5)
chips = product('chips',2,20,.50)
corner_store = store_inventory('corner_store')
corner_store.add_item(toilet_paper)
corner_store.add_item(chips)
inventory_dict = {'toilet paper': product('toilet paper',1,10,5), 'chips': product('chips',2,20,.50)}

# The store operation
print('\n'*100)
the_store_is_open = True
while the_store_is_open:
#    
    print('What would you like to do?')
    print('Make a sale, type 1')
    print('Update inventory of existing items, type 2')
    print('Add new product to inventory, type 3')
    print('Display total inventory, type 4')
    print('Lookup item from inventory, type 5')
    print('Close the store, type 6')
    player_choice = input('What function would you like? ')
    if player_choice == '1':
        print('\n'*100)
        make_a_sale()
    if player_choice == '2':
        print('\n'*100)
        update_inventory()
    if player_choice == '3':
        print('\n'*100)
        new_item('corner_store')
    if player_choice == '4':
        print('\n'*100)
        total = 0
        for i in inventory_dict:
            print(f'{inventory_dict[i].name} quantity: {inventory_dict[i].quantity} price: {inventory_dict[i].price}')
            total += (inventory_dict[i].quantity * inventory_dict[i].price)
        print(f'The total value is ${total}')
    if player_choice == '5':
        print('\n'*100)
        item_to_search = ''
        while item_to_search not in inventory_dict:
            item_to_search = input('What item would you like to lookup? ')
        print(inventory_dict[item_to_search])
    if player_choice == '6':
        the_store_is_open = False