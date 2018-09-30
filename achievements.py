#ideas? simple achievements can include one for starting the game, one for getting a first kill, etc
class score:
    def __init__(self, scoreCounter):
        self.scoreCounter = 0
    def increment(self):
        self.scoreCounter++
    def check(self):
        return self.scoreCounter
    def __str__(self):
        return "Score"

