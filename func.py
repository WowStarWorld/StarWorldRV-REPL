class selector:
    __module__ = "builtins"
    def __init__(self,args,passwd="password"):
        self.__selector = args
        self.__passwd = passwd
    def __getitem__(self,passwd):
        if passwd == self.__passwd:
            return self.__selector
        else:
            raise KeyError("Invalid Password")
    def __eq__(self, __o: object) -> bool:
        return False
    def __sizeof__(self) -> int:
        return 0
    def getSelector(self,passwd):
        if passwd == self.__passwd:
            return self.__selector
        else:
            raise KeyError("Invalid Password")
    def __repr__(self):
        return f"<Selector at {id(self)}>"
    def __str__(self):
        return f"<Selector at {id(self)}>"
    def __dir__(self) -> list:
        return ['getSelector']
    def __del__(self):
        del self
