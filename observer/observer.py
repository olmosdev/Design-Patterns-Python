from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def refresh(self, ticket_number):
        pass

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []
        self._tickets = 1

    def subscribe(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            print("Observer not found in the list.")

    def notify(self):
        for observer in self._observers:
            observer.refresh(self._tickets)
    
    def sell(self):
        self.notify()
        self._tickets += 1

# Observer implementations for demonstration

# This observer send an email notification when a ticket is sold
class SendMail(Observer):
    def refresh(self, ticket_number):
        print(f"Email sent for ticket number: {ticket_number}"  )

# This observer creates an invoice when a ticket is sold
class Invoice(Observer):
    def refresh(self, ticket_number):
        print(f"Invoice created for ticket number: {ticket_number}")

# Creating observers to get ready to subscribe to the subject
send_mail = SendMail()
invoice = Invoice()

subject = Subject()
subject.subscribe(send_mail)
subject.subscribe(invoice)

subject.sell()
subject.sell()
subject.sell()
subject.sell()

