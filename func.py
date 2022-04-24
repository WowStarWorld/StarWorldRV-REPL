import hashlib

class selector:
    __module__ = "builtins"
    def __init__(self,args,passwd="password"):
        self.__selector = args
        self.__password = hashlib.md5(str(passwd).encode(encoding='utf-8')).hexdigest()
    def __eq__(self, __o: object) -> bool:
        return False
    def __sizeof__(self) -> int:
        return 0
    def getSelector(self,passwd:str):
        __md5 = hashlib.md5(str(passwd).encode(encoding='utf-8')).hexdigest()
        if __md5 == self.__password:
            return self.__selector
        else:
            raise KeyError("Invalid Password")
    def __repr__(self):
        return f"[{hex(id(self))}]"
    def __str__(self):
        return f"[{hex(id(self))}]"
    def __dir__(self) -> list:
        return ['getSelector']
    def __del__(self):
        del self
