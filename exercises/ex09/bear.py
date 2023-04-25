"""File to define Bear class!"""


class Bear:
    """Defines bears."""

    age: int
    hunger_score: int
    
    def __init__(self):
        """Initializing age and hunger."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Changing values for every day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Changing the hunger score."""
        self.hunger_score += num_fish
    