from typing import Any, List
import time

"""
Duck typing is a programming concept, primarily used in dynamic languages like Python and Ruby, 
which determines an object's usability based on its methods and attributes rather than its explicit type or class. 
It follows the principle: "If it walks like a duck and it quacks like a duck, then it must be a duck". 
"""

class TaskList:
    def __init__(self, tasks: List[Any]):
        self.__tasks = tasks

    # "__iter__" is executed in the for loop. Return an iterable object
    def __iter__(self):
        return TaskIterator(self)

    def get_tasks(self) -> List[Any]:
        return self.__tasks

class TaskIterator:
    def __init__(self, task_list: TaskList):
        self.task_list = task_list
        self.index = 0

    # Something that is iterable must implement the "__next__" method
    def __next__(self) -> Any:
        if self.index < len(self.task_list.get_tasks()):
            task = self.task_list.get_tasks()[self.index]
            self.index += 1
            return task()
        else:
            raise StopIteration

def task1():
    return "Task 1 is executed."

def task2():
    return "Task 2 is executed."

def task3():
    return "Task 3 is executed."

tasks = [task1, task2, task3]
task_list = TaskList(tasks)

for task in task_list: # It is precisely at this point that the "__iter__" method is executed
    print(task)
    time.sleep(1)  # Simulate time delay between task executions


