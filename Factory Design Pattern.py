from abc import ABC, abstractmethod

#singleton payment gateway
class Paymentgateway:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new payment method now")
            cls._instance = super().__new__(cls)
        return cls._instance

    def process_payment(self, payment_method, amount):
        print(f"We are Processing payment of ${amount} via {payment_method.__class__.__name__}")
        payment_method.pay(amount)

#Abstract payment method(Factory)
class PaymentMethod(ABC):
    pass

@abstractmethod
def pay(self, amount):
    pass

#single example for each payment, we have Creditcard, PayPal, Bank Transfer, CryptoPayment, GooglePay, etc
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"We are Processing payment of ${amount} using credit card")

class Paypal(PaymentMethod):
    def pay(self, amount):
        print(f"We are Processing payment of ${amount} using Paypal")

class BankTransfer(PaymentMethod):
    def pay(self, amount):
        print(f"We are Processing payment of ${amount} using bank transfer")

class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        print(f"We are Processing payment of ${amount} using crypto payment")

class GooglePay(PaymentMethod):
    def pay(self, amount):
        print(f"We are Processing payment of ${amount} using google payment")

# Create Payment Method Objects(Factory)
class PaymentFactory:
       @staticmethod
       def create_payment(method_type):
           method_type = method_type.lower()
           if method_type == "creditcard":
               return CreditCard()
           elif method_type == "banktransfer":
                return BankTransfer()
           elif method_type == "cryptopay":
               return CryptoPayment()
           elif method_type == "paypal":
               return Paypal()
           elif method_type == "googlepay":
               return GooglePay()

if __name__ == "__main__":
    gateway1 = Paymentgateway()
    payment_methods = ["creditcard", "banktransfer", "cryptopay", "paypal", "googlepay"]

    for method_name in payment_methods:
        method = PaymentFactory.create_payment(method_name)
        gateway1.process_payment(method, amount=100)




