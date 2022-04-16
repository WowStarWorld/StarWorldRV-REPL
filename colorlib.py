import rich.console
import json
from js2py.base import JsObjectWrapper

consoles = rich.console.Console()
def cprint(text:str,color:str,end:str="\n"):
    self = consoles
    try:
        dicts = text.to_dict()
        jsons = {}
        for key,value in dicts.items():
            if type(value) == JsObjectWrapper:
                jsons[key] = f"[bold blue]{str(value)}[/bold blue]".replace("\\'","\\\"").replace('\'',"")
            elif type(value) == type(json):
                jsons[key] = f"[bold purple]{str(value)}[/bold purple]"
            elif type(value) == type:
                jsons[key] = f"[blue]{str(value)}[/blue]"
            elif type(value) == str:
                jsons[key] = f"\'[bold yellow]{str(value)}[/bold yellow]\'"
            else:
                jsons[key] = f"{str(value)}"
        self.print(f"[{color.lower()}]{json.dumps(jsons,indent=2)}[/{color.lower()}]".replace("\\\\\\\\","\\\\").replace("\\\"","").replace("\"","").replace("\'",'"'),end=end)
    except :
        self.print(f"[{color.lower()}]{text}[/{color.lower()}]",end=end)
def cinput(text:str,color:str):
    self = consoles
    return self.input(f"[{color.lower()}]{text}[/{color.lower()}]")