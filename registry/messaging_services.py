class ConnectorRegistry:
    def __init__(self, name):
        """Initialize the registry instance with a custom name."""
        self._name = name
        self._registry = {}

    def register(self, key=None):
        """
        Decorator that registers a function.
        If no key is provided, it uses the function's name.
        """
        def decorator(func):
            # Using the logic from your structure: key or function name
            register_key = key or func.__name__.lower()
            self._registry[register_key] = func
            return func
        return decorator

    def get(self, key):
        """Retrieve the registered function by its key."""
        if key not in self._registry:
            raise KeyError(f"Service '{key}' not found in registry '{self._name}'")
        return self._registry[key]

    def list_all(self):
        """Returns a list of all registered message services."""
        return list(self._registry.keys())

# --- Practical Example: Messaging Services ---

# We create our registry for notification services
messenger = ConnectorRegistry("NotificationSystem")

@messenger.register(key="whatsapp")
def send_whatsapp(recipient, message):
    """Logic to send a WhatsApp message."""
    return f"WhatsApp sent to {recipient}: {message}"

@messenger.register() # This will be registered as 'send_email'
def send_email(recipient, message):
    """Logic to send an Email."""
    return f"Email sent to {recipient}: {message}"

@messenger.register(key="sms")
def send_sms(recipient, message):
    """Logic to send a traditional SMS."""
    return f"SMS sent to {recipient}: {message}"

# --- Execution ---

def notify_user(service_type, user_contact, text):
    """Generic function that uses the registry to notify users."""
    try:
        # Get the function directly from the registry
        send_func = messenger.get(service_type)
        # Execute the function
        print(send_func(user_contact, text))
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    print(f"Registry: {messenger._name}")
    print(f"Supported Services: {messenger.list_all()}\n")

    # Real-world usage simulation
    notify_user("whatsapp", "+52 33123456", "Your order is ready!")
    notify_user("send_email", "user@example.com", "Welcome to our platform!")
    notify_user("sms", "+52 55987654", "Your verification code is 4432")
    notify_user("toms", "+52 55987654", "Your verification code is 4432")