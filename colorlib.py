import rich.console
import json
from js2py.base import JsObjectWrapper

consoles = rich.console.Console()
def cprint(text,color:str,end:str="\n"):
    self = consoles
    try:
        try:
            text:JsObjectWrapper = text
            is_list = True
            try:
                lists = text.to_dict()
                for keys,values in lists.items():
                    try:
                        int(keys)
                    except:
                        is_list = False
            except:
                lists = text.to_list()
                is_list = True
            if not is_list:
                raise Exception()
            self.print("[")
            for value in lists:    
                if type(value) == JsObjectWrapper:
                    try:
                        self.print(f"  [bold blue]{str(value)}[/bold blue],".replace("\\'","\\\"").replace('\'',""))
                    except:
                        pass
                elif type(value) == type(json):
                    try:self.print(f"  [bold purple]{str(value)}[/bold purple],")
                    except:pass
                elif type(value) == type:
                    try:self.print(f"  [blue]{str(value)}[/blue],")
                    except:pass
                elif type(value) == str:
                    try:
                        self.print(f"  \'[bold yellow]{str(value)}[/bold yellow]\',")
                    except:pass
                else:
                    try:
                        self.print(f"  {str(value)},")
                    except:
                        pass
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
                    try:jsons[f"\'{key}\'"] = f"[bold purple]{str(value)}[/bold purple]"
                    except:pass
                elif type(value) == type:
                    try:jsons[f"\"{key}\'"] = f"[blue]{str(value)}[/blue]"
                    except:pass
                elif type(value) == str:
                    try:jsons[f"\'{key}\'"] = f"\'[bold yellow]{str(value)}[/bold yellow]\'"
                    except:pass
                else:
                    try:
                        jsons[f"\'{key}\'"] = f"{str(value)}"
                    except:
                        pass
            if jsons == {}:
                self.print(text)
            else:
                self.print(f"[{color.lower()}]{json.dumps(jsons,indent=2)}[/{color.lower()}]".replace("\\\\\\\\","\\\\").replace("\\\"","").replace("\"","").replace("\'",'"'),end=end)
        except :
            self.print(f"[{color.lower()}]{text}[/{color.lower()}]",end=end)
def cinput(text:str,color:str):
    self = consoles
    return self.input(f"[{color.lower()}]{text}[/{color.lower()}]")