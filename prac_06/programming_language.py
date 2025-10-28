"""
Programming Languages
Estimate: 30 mins
Actual:35 mins
"""



class ProgrammingLanguage:
    def __init__(self,name = "", typing = "", reflection = "", year = 0):
        """Initialise programming language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __repr__(self):
        """returns string of name of programming language"""
        return f"{self.name}"

    def is_dynamic(self):
        """Returns True if programming language 'typing' is Dynamic"""
        return self.typing == "Dynamic"



