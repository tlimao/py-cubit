from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

T = TypeVar('T')

class CubitListener(ABC, Generic[T]):
    
    @abstractmethod
    def on_state_change(self, new_state: T) -> None:
        """
        Method to be called when the Cubit's state changes.
        
        Args:
            new_state (T): The new state emitted by the Cubit.
        """
        pass

class Cubit(Generic[T]):
    
    def __init__(self, state: T) -> None:
        """
        Initializes the Cubit with an initial state.

        Args:
            state (T): The initial state of the Cubit.
        """
        self._state: T = state
        self._listeners: List[CubitListener[T]] = []

    @property
    def state(self) -> T:
        """
        Returns the current state of the Cubit.

        Returns:
            T: The current state.
        """
        return self._state

    def emit(self, new_state: T):
        """
        Updates the state and notifies all registered listeners.

        Args:
            new_state (T): The new state to emit.
        """
        self._state = new_state
        for listener in self._listeners:
            listener.on_state_change(new_state)

    def add_listener(self, listener: CubitListener[T]):
        """
        Adds a listener that will be notified of state changes.

        Args:
            listener (CubitListener[T]): The listener to add.

        Raises:
            TypeError: If the listener does not implement `CubitListener`.
        """
        if not isinstance(listener, CubitListener):
            raise TypeError("Listener must implement CubitListener.")
        self._listeners.append(listener)

    def remove_listener(self, listener: CubitListener[T]):
        """
        Removes a listener.

        Args:
            listener (CubitListener[T]): The listener to remove.
        """
        self._listeners.remove(listener)
    