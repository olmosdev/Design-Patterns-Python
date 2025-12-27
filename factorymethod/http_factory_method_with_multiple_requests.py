"""HTTP Factory Method example.

Demonstrates the Factory Method pattern to separate the creation of an HTTP request
object (HttpGet) from its usage. At the bottom of the module a factory instance is
created, it produces a product (HttpGet) and the product is used to perform a request.
"""
import http.client
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor, as_completed

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

# Concurrent requests using ThreadPoolExecutor.
# This does not modify the existing HttpGet implementation.
# HttpGet.request creates a new HTTPSConnection per call, so reusing http_get across threads is safe.

def do_request(i: int) -> str | None:
    # Use the existing http_get product to perform the request.
    return http_get.request(i)

if __name__ == "__main__":
    # IDs to request concurrently
    ids = list(range(2, 6))

    # Create a thread pool and submit requests.
    # Each future runs http_get.request(i) in a separate worker thread.
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(do_request, i): i for i in ids}

        # as_completed yields futures as they finish (non-blocking main thread while waiting).
        for fut in as_completed(futures):
            idx = futures[fut]
            try:
                result = fut.result()
                print(f"Result for id={idx}:\n{result}\n")
            except Exception as e:
                print(f"Request id={idx} failed: {e}")