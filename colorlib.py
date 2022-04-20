import rich.console
import json
from js2py.base import JsObjectWrapper

consoles = rich.console.Console()
def cprint(text,color:str,end:str="\n"):
    self = consoles
    try:
        try:
            text:JsObjectWrapper = text
            lists = text.to_list()
            self.print("[")
            for value in lists:    
                if type(value) == JsObjectWrapper:
                    try:
                        self.print(f"  [bold blue]{str(value)}[/bold blue],".replace("\\'","\\\"").replace('\'',""))
                    except:
                        pass
                elif type(value) == type(json):
                    self.print(f"  [bold purple]{str(value)}[/bold purple],")
                elif type(value) == type:
                    self.print(f"  [blue]{str(value)}[/blue],")
                elif type(value) == str:
                    self.print(f"  \'[bold yellow]{str(value)}[/bold yellow]\',")
                else:
                    self.print(f"  {str(value)},")
            self.print("]")
        except:
            raise Exception()
    except:
        try:
            text:JsObjectWrapper = text
            dicts = text.to_dict()
            jsons = {}
            for key,value in dicts.items():
                if type(value) == JsObjectWrapper:
                    try:
                        jsons[f"\'key\'"] = f"[bold blue]{str(value)}[/bold blue]".replace("\\'","\\\"").replace('\'',"")
                    except:
                        pass
                elif type(value) == type(json):
                    jsons[f"\'{key}\'"] = f"[bold purple]{str(value)}[/bold purple]"
                elif type(value) == type:
                    jsons[f"\"{key}\'"] = f"[blue]{str(value)}[/blue]"
                elif type(value) == str:
                    jsons[f"\'{key}\'"] = f"\'[bold yellow]{str(value)}[/bold yellow]\'"
                else:
                    jsons[f"\'{key}\'"] = f"{str(value)}"
            if jsons == {}:
                self.print(text)
            else:
                self.print(f"[{color.lower()}]{json.dumps(jsons,indent=2)}[/{color.lower()}]".replace("\\\\\\\\","\\\\").replace("\\\"","").replace("\"","").replace("\'",'"'),end=end)
        except :
            self.print(f"[{color.lower()}]{text}[/{color.lower()}]",end=end)
def cinput(text:str,color:str):
    self = consoles
    return self.input(f"[{color.lower()}]{text}[/{color.lower()}]")