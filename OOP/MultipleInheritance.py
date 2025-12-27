class SMS:
    def send(self) -> None:
        print("Sent by SMS.")

class Saver:
    def save(self) -> None:
        print("Saved in a database")

class Email:
    def send(self) -> None:
        print("Message sent by email.")

# The class furthest to the left has the highest priority.
class Sale(SMS, Saver, Email):
    pass

sale = Sale()
sale.send()
sale.save()