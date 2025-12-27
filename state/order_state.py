from abc import ABC, abstractmethod

class OrderState(ABC):
    @abstractmethod
    def pay(self, order):
        pass

    def ship(self, order):
        pass

    def deliver(self, order):
        pass

class NewOrderState(OrderState):
    def pay(self, order):
        print("The order has been successfully paid!.")
        order.set_state(PaidOrderState())

    def ship(self, order):
        print("It cannot be sent without payment")

    def deliver(self, order):
        print("It cannot be delivered without being paid for")

class PaidOrderState(OrderState):
    def pay(self, order):
        print("The order has already been paid for.")

    def ship(self, order):
        print("The order has been successfully shipped!.")
        order.set_state(ShippedOrderState())

    def deliver(self, order):
        print("It cannot be delivered without being sent first.")

class ShippedOrderState(OrderState):
    def pay(self, order):
        print("The order has already been paid for.")

    def ship(self, order):
        print("The order has already been shipped.")

    def deliver(self, order):
        print("The order has been successfully delivered!.")
        order.set_state(DeliveredOrderState())

class DeliveredOrderState(OrderState):
    def pay(self, order):
        print("The order has already been paid for.")

    def ship(self, order):
        print("The order has already been shipped.")

    def deliver(self, order):
        print("The order has already been delivered.")

class Order:
    def __init__(self, state: OrderState):
        self.state = state

    def set_state(self, state: OrderState):
        self.state = state

    def pay(self):
        self.state.pay(self)
    
    def ship(self):
        self.state.ship(self)

    def deliver(self):
        self.state.deliver(self)

order = Order(NewOrderState())
order.ship()
order.deliver()

order.pay()
order.deliver()
order.ship()
order.deliver()

order.pay()