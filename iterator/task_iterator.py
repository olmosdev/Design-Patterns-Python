from time import time
from abc import ABC, abstractmethod
from typing import Any, List
import time

"""
First-class functions: A first-class function in functional programming is a 
function that can be stored in a variable
"""

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

class TaskList(IterableCollection):
    def __init__(self, tasks: List[Any]):
        self.__tasks = tasks

    def create_iterator(self) -> Iterator:
        return TaskIterator(self)
    
    def get_tasks(self) -> List[Any]:
        return self.__tasks

class TaskIterator(Iterator):
    def __init__(self, task_list: TaskList):
        self.task_list = task_list
        self.index = 0

    def next(self) -> Any:
        if self.has_next():
            task = self.task_list.get_tasks()[self.index]
            self.index += 1
            return task()

    def has_next(self) -> bool:
        return self.index < len(self.task_list.get_tasks())

def task1():
    return "Task 1 is executed."

def task2():
    return "Task 2 is executed."

def task3():
    return "Task 3 is executed."

tasks = [task1, task2, task3]
task_list = TaskList(tasks)
task_iterator = task_list.create_iterator()

while task_iterator.has_next():
    print(task_iterator.next())
    time.sleep(1)  # Simulate time delay between task executions
print(task_iterator.next())

