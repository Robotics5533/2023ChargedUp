class DotDict:
    def __init__(self, dictionary):
        self.__dict__ = dictionary

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return DotDict(self.__dict__[attr])
        return None