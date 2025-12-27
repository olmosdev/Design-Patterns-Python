"""HTTP Factory Method example.

Demonstrates the Factory Method pattern to separate the creation of an HTTP request
object (HttpGet) from its usage. At the bottom of the module a factory instance is
created, it produces a product (HttpGet) and the product is used to perform a request.
"""
import http.client
from abc import ABC, abstractmethod

class HttpRequest(ABC):
    """Abstract interface for objects that perform HTTP requests.

    Methods:
    - request(id: int) -> str | None: perform the request and return the response body
      as str, or None on error.
    """
    @abstractmethod
    def request(self, id: int) -> str:
        pass

class HttpGet(HttpRequest):
    """Concrete HttpRequest implementation performing HTTP GET requests to a domain/path."""
    def __init__(self, domain: str, path: str) -> None:
        self.__domain = domain
        self.__path = path

    def request(self, id: int) -> str | None:
        conn = http.client.HTTPSConnection(self.__domain)
        conn.request("GET", f"/{self.__path}/{id}")
        response = conn.getresponse()

        if response.status == 200:
            data = response.read()
            return data.decode("utf-8")
        else:
            print(f"Error in the request. Error: {response.status} - {response.reason}")

        conn.close()

class HttpRequestFactory(ABC):
    """Abstract factory that defines the contract to create HttpRequest instances."""
    def __init__(self, domain: str, path: str) -> None:
        self._domain = domain
        self._path = path

    @abstractmethod
    def create(self) -> HttpRequest:
        pass

class HttpGetFactory(HttpRequestFactory):
    """Concrete factory that creates HttpGet instances."""
    def create(self) -> HttpRequest:
        return HttpGet(self._domain, self._path)

# Factory instance created here: the factory knows how to build HttpGet products
http_get_factory = HttpGetFactory("jsonplaceholder.typicode.com", "posts")

# Product created here: the factory produces the HttpGet object (the product)
http_get = http_get_factory.create()

# Using the created product: perform the request using the object produced by the factory
res = http_get.request(1)
print(res)
