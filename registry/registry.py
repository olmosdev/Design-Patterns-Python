class ConnectorRegistry:
    """Central registry to manage different database connectors."""
    _connectors = {}

    @classmethod
    def register(cls, name):
        """Decorator to register a class with a specific name."""
        def wrapper(wrapped_class):
            cls._connectors[name] = wrapped_class()
            return wrapped_class
        return wrapper

    @classmethod
    def get(cls, name):
        """Retrieve a registered instance by name."""
        if name not in cls._connectors:
            raise KeyError(f"Connector '{name}' not found in registry.")
        return cls._connectors[name]

# --- Real-world usage ---

@ConnectorRegistry.register("mysql")
class MySQLService:
    def query(self, sql):
        return f"MySQL: Executing {sql}"

@ConnectorRegistry.register("mongodb")
class MongoService:
    def query(self, sql):
        return f"MongoDB: Finding document {sql}"

# --- Execution ---

def run_app(db_type):
    # The app doesn't care about the implementation, only the key
    try:
        db = ConnectorRegistry.get(db_type)
        print(db.query("SELECT * FROM users"))
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    run_app("mysql")    # Output: MySQL: Executing SELECT * FROM users
    run_app("mongodb")  # Output: MongoDB: Finding document SELECT * FROM users