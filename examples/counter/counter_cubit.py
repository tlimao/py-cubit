from pycubit.cubit import Cubit



class CounterCubit(Cubit[int]):
    
    def __init__(self):
        """
        Initializes the CounterCubit with a default state of count = 0.
        """
        super().__init__(0)

    def increment(self):
        """
        Increments the count by 1.
        """
        self.emit(self.state + 1)

    def decrement(self):
        """
        Decrements the count by 1.
        """
        self.emit(self.state - 1)