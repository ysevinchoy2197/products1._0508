class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print(f"nomi: {self.name}, narxi: {self.price}")

p1 = Product("Olma", "10000")
p2 = Product("Uzum", "15000")
p3 = Product("Anjir", "22000")
p4 = Product("Anor", "27000")

print(p1.name)

roy = [p1, p2, p3, p4]
print(roy[0].name)
print(roy[0].price)
