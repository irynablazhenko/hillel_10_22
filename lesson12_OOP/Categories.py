
class Categories:
    count = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id
        Categories.count += 1

    def change_name(self, new_name):
        self.name = new_name

    def item_info(self):
        print(f'Категория: {self.name}, идентификатор: {self.id}')