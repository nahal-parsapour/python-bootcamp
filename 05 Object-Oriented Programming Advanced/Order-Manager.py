# Practice week5 with an Order_Manager System
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} USD"


class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"User: {self.username}"


class Admin(User):
    def __init__(self, username):
        super().__init__(username)

    def add_product(self, store, product):
        store.add_product(product)
        print(f"Admin {self.username} added product '{product.name}'.")


class DiscountEngine:
    def __init__(self, percent=0):
        self.percent = percent

    def apply_discount(self, total):
        if self.percent <= 0:
            return total
        discount_amount = total * (self.percent / 100)
        return total - discount_amount


class Order:
    def __init__(self, user, discount_engine=None):
        self.user = user
        self.items = []
        self.discount_engine = discount_engine or DiscountEngine(0)

    def add_item(self, product, quantity=1):
        self.items.append((product, quantity))
        print(f"Added {quantity} x '{product.name}' to order.")

    def total(self):
        total = sum(p.price * q for p, q in self.items)
        return self.discount_engine.apply_discount(total)

    def report(self):
        print(f"Order report for {self.user.username}:")
        for product, qty in self.items:
            print(f" - {qty} x {product.name} @ {product.price} USD")

        print(f"Total (after discount): {self.total()} USD")

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print(f"Products in {self.name}:")
        for p in self.products:
            print(" -", p)


if __name__ == "__main__":
    store = Store("Online Shop")
    admin = Admin("admin1")

    p1 = Product("Laptop", 1200)
    p2 = Product("Mouse", 25)

    admin.add_product(store, p1)
    admin.add_product(store, p2)

    store.list_products()

    user = User("nahal")
    discount = DiscountEngine(percent=20)
    order = Order(user, discount_engine=discount)

    order.add_item(p1, 1)
    order.add_item(p2, 2)

    order.report()