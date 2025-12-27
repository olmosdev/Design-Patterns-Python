from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, context): # This function receive the context, the sabe object that is executing this
        pass

class ProcessContext:
    def __init__(self, state: State):
        self._state = state

    def set_state(self, state: State):
        self._state = state

    def request(self):
        self._state.handle(self)

class StartState(State):
    def handle(self, context: ProcessContext):
        print("State: Starting. Moving to execution.")
        context.set_state(RunState())

class RunState(State):
    def handle(self, context: ProcessContext):
        print("State: Running. Moving to completion.")
        context.set_state(EndState())

class EndState(State):
    def handle(self, context: ProcessContext):
        print("State: Finished.")

process = ProcessContext(StartState())
process.request()
process.request()
process.request()
process.request()

