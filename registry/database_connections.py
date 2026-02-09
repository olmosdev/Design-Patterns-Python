class ConnectorRegistry:
    def __init__(self, name):
        """Initialize the registry instance with a custom name."""
        self._name = name
        self._registry = {}

    def register(self, key=None):
        """
        Decorator that registers a class. 
        If no key is provided, it uses the class name in lowercase.
        """
        def decorator(func_or_class):
            # Use provided key or the name of the object
            register_key = key or func_or_class.__name__.lower()
            self._registry[register_key] = func_or_class
            return func_or_class
        return decorator

    def get(self, key):
        """Retrieve the registered class by its key."""
        if key not in self._registry:
            raise KeyError(f"'{key}' not found in registry '{self._name}'")
        return self._registry[key]

    def list_all(self):
        """Returns a list of all registered keys."""
        return list(self._registry.keys())

# --- Practical Example: Database connections ---

# We create the registry instance
db_registry = ConnectorRegistry("DatabaseCluster")

# Registering using a custom key
@db_registry.register(key="mysql")
class MySQLConnector:
    def __init__(self, name):
        self._name = name
    def connect(self):
        return f"Connecting to MySQL: {self._name}"

# Registering without a key (it will use 'postgresconnector' automatically)
@db_registry.register()
class PostgresConnector:
    def __init__(self, name):
        self._name = name
    def connect(self):
        return f"Connecting to Postgres: {self._name}"

# --- Execution ---

if __name__ == "__main__":
    print(f"Registry Name: {db_registry._name}")
    print(f"Registered keys: {db_registry.list_all()}")

    # We 'get' the class from the registry and then instantiate it
    storage_class = db_registry.get("mysql")
    storage_instance = storage_class("Main_Prod")
    
    print(storage_instance.connect())