from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paid {amount} with credit card {self.card_number}")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def pay(self, amount):
        print(f"Paid {amount} with PayPal account {self.email}")


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} has total {self.name}"


# Context
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def pay(self, payment_strategy):
        amount = self.calculate_total()
        payment_strategy.pay(amount)


cart = ShoppingCart()
cart.add_item(Item("Shirt", 50.0))
cart.add_item(Item("Jeans", 100.0))

credit_card = CreditCardPayment("1234567890123456", "12/24", "123")
paypal = PayPalPayment("johndoe@gmail.com", "password123")

cart.pay(credit_card)
cart.pay(paypal)
