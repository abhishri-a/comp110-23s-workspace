"""File to define Fish class!"""


class Fish:
    """Defines fish."""

    age: int
    
    def __init__(self):
        """Initializing age and hunger."""
        self.age = 0   
        return None
    
    def one_day(self):
        """Changing daily values."""
        self.age += 1
        return None