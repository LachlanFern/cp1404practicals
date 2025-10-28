"""
Programming Languages
Estimate: 30 mins
Actual:
"""



class ProgrammingLanguage:
    def __init__(self,name = "", typing = "", reflection = "", year = 0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __repr__(self):
        return f"{self.name}\n"

    def is_dynamic(self):
        return self.typing == "Dynamic"



