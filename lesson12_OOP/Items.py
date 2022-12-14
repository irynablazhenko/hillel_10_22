


class Items:
    count = 0

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        Items.count += 1

    def change_name(self, new_name):
        self.name = new_name

    def change_price(self, new_price):
        self.price = new_price

    def change_weight(self, new_weight):
        self.weight = new_weight

    def item_info(self):
        print(f'Товар: {self.name}, цена: {self.price}, вес {self.weight}')

