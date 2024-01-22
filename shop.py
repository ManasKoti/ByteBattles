class Shop:
    
    def __init__(self, items):
        self.items = items
        
    def display_items(self, player):
        print("Here are the items for sale:")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item[0]} - {item[1]} gold")
        print(f"{len(self.items) + 1}. Exit")
        print(f"You have {player.money} gold.\n")
            
    def buy_item(self, item_number, player):
        if item_number == len(self.items) + 1:
            return
        item_name, item_price = self.items[item_number - 1]
        if player.money >= item_price:
            player.money -= item_price
            player.inventory.append(item_name)
            print(f"You bought {item_name} for {item_price} gold.")
            print(f"You now have {player.money} gold.\n")
        else:
            print("You don't have enough gold.\n")