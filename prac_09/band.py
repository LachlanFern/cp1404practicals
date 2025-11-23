
class Band:
    def __init__(self, name=""):
        """Construct band with list of empty musicians"""
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        return str(vars(self))

    def add(self, musician):
        """add musicians to band collection"""
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            print(musician.play())
