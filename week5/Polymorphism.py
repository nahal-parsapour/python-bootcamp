# Polymorphism
class PayPal:
    def pay(self, amount):
        print(f"Paypal: paying ${amount}")


class CreditCard:
    def pay(self, amount):
        print(f"CreditCard: charging ${amount} to card.")


class Crypto:
    def pay(self, amount):
        print(f"Crypto: sending ${amount} equivalent in crypto.")


def process_payments(payments, amount):
    for method in payments:
        method.pay(amount)


if __name__ == "__main__":
    paypal = PayPal()
    card = CreditCard()
    crypto = Crypto()

    methods = [paypal, card, crypto]
    process_payments(methods, 100)