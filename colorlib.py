import rich.console
import json
from js2py.base import JsObjectWrapper

consoles = rich.console.Console()
def cprint(text:str,color:str,end:str="\n"):
    self = consoles
    self.print(f"[{color.lower()}]{text}[/{color.lower()}]",end=end)
def cinput(text:str,color:str):
    self = consoles
    return self.input(f"[{color.lower()}]{text}[/{color.lower()}]")