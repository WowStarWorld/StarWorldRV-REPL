import rich.console
import json
from js2py.base import JsObjectWrapper


def is_infinite_loop_object(l):
    if type(l) == list:
        for i in l:
            if type(i) == list: is_infinite_loop_object(i)
            elif type(i) == dict: is_infinite_loop_object(i)
    if type(l) == dict:
        for i in l.values():
            if type(i) == list: is_infinite_loop_object(i)
            elif type(i) == dict: is_infinite_loop_object(i)



list1 = []
consoles = rich.console.Console()
def cprint(text,color:str,end:str="\n",indent:int=0):
    self = consoles
    indents = " " * indent
    this = cprint
    global list1
    try:
        try:
            text:JsObjectWrapper = text
            is_list = True
            if type(text) != list:
                try:
                    r = text.to_dict()
                    for keys,values in r.items():
                        try:
                            int(keys)
                        except:
                            is_list = False
                except:
                    lists1 = text.to_list()
                    if lists1 == []:
                        is_list = False
                    elif type(lists1) == dict:
                        is_list = True
                    else:
                        is_list = True
            else:
                is_list = True
            if not is_list:
                raise Exception()
            try:
                lists1 = text.to_list()
            except:
                try:
                    lists1 = text
                except:
                    raise Exception()
            self.print(f"{indents}[")
            for value in lists1:    
                if type(value) == JsObjectWrapper:
                    try:
                        self.print(f"{indents}  [bold blue]{str(value)}[/bold blue],".replace("\\'","\\\"").replace('\'',""))
                    except:
                        pass
                elif type(value) == type(json):
                    try:self.print(f"{indents}  [bold purple]{str(value)}[/bold purple],")
                    except:pass
                elif type(value) == type:
                    try:self.print(f"{indents}  [blue]{str(value)}[/blue],")
                    except:pass
                elif type(value) == str:
                    try:
                        self.print(f"{indents}  \'[bold yellow]{str(value)}[/bold yellow]\',")
                    except:pass
                elif type(value) == type(None):
                    try:
                        self.print(f"{indents}  [italic bold black]undefined[/italic bold black],")
                    except:pass
                elif type(value) == list or type(value) == dict:
                    try:
                        try:
                            is_infinite_loop_object(value)
                            this(value,color,end="\n",indent=indent+2)
                        except:
                            this(f"[bold red][...][/bold red],",color,indent=indent+2)
                    except:pass
                else:
                    try:
                        self.print(f"{indents}  {str(value)},")
                    except:
                        pass
            self.print(f"{indents}]")
        except:
            raise Exception()
    except:
        try:
            text:JsObjectWrapper = text
            try:
                dicts = text.to_dict()
            except:
                if type(text) == dict:
                    dicts = text
                else:
                    raise Exception()
            print(f"{indents}"+"{")
            for key,value in dicts.items():
                if type(value) == JsObjectWrapper:
                    try:
                        self.print(f"{indents}  \'{key}\'"+":"+f"[bold blue]{str(value)}[/bold blue]".replace("\\'","\\\"").replace('\'',""))
                    except:
                        pass
                elif type(value) == type(json):
                    try:
                        self.print(f"{indents}  \'{key}\'"+":"+f"[bold purple]{str(value)}[/bold purple]")
                    except:pass
                elif type(value) == type:
                    try:
                        self.print(f"{indents}  \"{key}\""+":"+f"[blue]{str(value)}[/blue]")
                    except:pass
                elif type(value) == str:
                    try:
                        self.print(f"{indents}  \'{key}\'"+":"+f"\'[bold yellow]{str(value)}[/bold yellow]\'")
                    except:pass
                elif type(value) == type(None):
                    try:
                        self.print(f"{indents}  \"{key}\""+":"+f"[italic bold black]undefined[/italic bold black]")
                    except:pass
                elif type(value) == list or type(value) == dict:
                    try:
                        try:
                            is_infinite_loop_object(value)
                            this(value,color,end="\n",indent=indent+2)
                        except:
                            this(f"\"{key}\""+":"+f"[bold red][...][/bold red],",color,indent=indent+2)
                    except:pass
                else:
                    try:
                        self.print(f"{indents}  \"{key}\""+":"+f"{str(value)}")
                    except:
                        pass
            print(f"{indents}"+"}")
        except :
            self.print(f"{indents}[{color.lower()}]{text}[/{color.lower()}]",end=end)
def cinput(text:str,color:str):
    self = consoles
    return self.input(f"[{color.lower()}]{text}[/{color.lower()}]")