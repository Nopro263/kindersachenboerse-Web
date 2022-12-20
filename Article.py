class Article:
    def __init__(self, lid, name, size, price, deleted):
        self.lid = lid
        self.name = name
        self.price = price
        self.size = size
        self.deleted = deleted

    def delete(self):
        self.deleted = True