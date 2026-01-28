from abc import ABC, abstractmethod
from typing import Any, List

class Iterator(ABC):
    @abstractmethod
    def next(self) -> Any:
        """Return the next item from the iterator."""
        pass

    @abstractmethod
    def has_next(self) -> bool:
        """Return True if there are more items to iterate over."""
        pass

class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        """Return an iterator for the collection."""
        pass

class ConcreteCollection(IterableCollection):
    def __init__(self, items: List[Any]):
        self._items = items

    def create_iterator(self) -> Iterator:
        return ConcreteIterator(self)

    def get_items(self) -> List[Any]:
        return self._items

class ConcreteIterator(Iterator):
    def __init__(self, collection: ConcreteCollection):
        self._collection = collection
        self._index = 0

    def next(self) -> Any:
        if self.has_next():
            item = self._collection.get_items()[self._index]
            self._index += 1
            return item

    def has_next(self) -> bool:
        return self._index < len(self._collection.get_items())

collection = ConcreteCollection(["Sara", "Tom", "John"])
iterator = collection.create_iterator()

while iterator.has_next():
    print(iterator.next())
print(iterator.next())

