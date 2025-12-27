from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def __init__(self, user, pwd, url, port):
        self.user = user
        self.pwd = pwd
        self.url = url
        self.port = port

    def send(self, message):
        print(f"Sending email with content: {message}")

class SMSNotification(Notification):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def send(self, message):
        print(f"Sending SMS with content: {message}")

class NotificationManager:
    """
    NotificationManager created without applying Dependency Injection.

    This implementation constructs a concrete Notification (SMSNotification) internally,
    coupling NotificationManager to that specific implementation.

    Consequences:
    - Makes unit testing harder because dependencies cannot be easily substituted.
    - Reduces flexibility to change the notification channel at runtime or configuration.
    - Violates the Dependency Inversion Principle and increases coupling.

    Recommendation:
    - Receive the dependency via constructor injection or a setter:
        def __init__(self, notification: Notification): ...
    - Or use a factory/provider to create the concrete implementation outside this class.
    """
    def __init__(self):
        # It is not good practice to construct service objects or other classes directly in the constructor.
        # self._notification = EmailNotification("enterprise", "enterprise_pwd", "smtp.enterprise.com", 3344)
        self._notification = SMSNotification("enterprise", "enterprise_pwd")

    def notify(self, message):
        self._notification.send(message)

class BetterNotificationManager:
    """
    BetterNotificationManager — applies Dependency Injection (constructor injection).

    This class receives a Notification implementation via its constructor.

    Parameters:
    - notification: Notification
        Any instance that implements the Notification interface (e.g. EmailNotification, SMSNotification).
        
    Benefits:
    - Decouples the sending logic from this manager.
    - Facilitates unit testing (mocks or stubs can be injected).
    - Allows changing the notification channel without modifying this class.
    """
    def __init__(self, notification: Notification):
        self._notification = notification

    def notify(self, message):
        self._notification.send(message)

notification_manager = NotificationManager()
notification_manager.notify("This is a notification message.")
print()

email_notification = EmailNotification("enterprise", "enterprise_pwd", "smtp.enterprise.com", 3344)
sms_notification = SMSNotification("enterprise", "enterprise_pwd")
better_notification_manager = BetterNotificationManager(email_notification)
better_notification_manager.notify("This is a notification message via Email.")
better_notification_manager = BetterNotificationManager(sms_notification)
better_notification_manager.notify("This is a notification message via SMS.")


