import os,sys,colorlib,platform,requests
import datetime
from time import sleep


version = "6.7.6"
def getAttributes(obj):
    attrs_list = []
    try:
        for i in range(len(dir(obj))-1):    
                if not dir(obj)[i].startswith("__") and dir(obj)[i] != "this" and dir(obj)[i] != "self" and dir(obj)[i] != "value":
                    attrs_list += [getattr(obj,dir(obj)[i])]
    except:pass
    return attrs_list
            
def helps():
    colorlib.cprint("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓","yellow")
    colorlib.cprint("┃                 RV REPL HELP PAGE                 ┃","Yellow")
    colorlib.cprint("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛","Yellow")
    colorlib.cprint("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓","Yellow")
    colorlib.cprint("┃ | REPL Commands:                                  ┃","Yellow")
    colorlib.cprint("┃     [bold yellow].help[/bold yellow]     [bold blue]Print help message[/bold blue]                  ┃","Yellow") 
    colorlib.cprint("┃     [bold yellow].about[/bold yellow]    [bold blue]Print about message[/bold blue]                 ┃","Yellow")
    colorlib.cprint("┃     [bold yellow].editor[/bold yellow]   [bold blue]Start REPL Code Editor[/bold blue]              ┃","Yellow")
    colorlib.cprint("┃     [bold yellow].exit[/bold yellow]     [bold blue]Exit the REPL[/bold blue]                       ┃","Yellow")
    colorlib.cprint("┃     [bold yellow].clear[/bold yellow]    [bold blue]Clear stored StarWorldScript[/bold blue]        ┃","Yellow")
    colorlib.cprint("┃     [bold yellow].load[/bold yellow]     [bold blue]Run the entered StarWorldScript[/bold blue]     ┃","Yellow")
    colorlib.cprint("┃     [bold yellow].debug[/bold yellow]    [bold blue]Run StarWorldScript and return Tree[/bold blue] ┃","Yellow")
    colorlib.cprint("┃     [bold yellow].cls[/bold yellow]      [bold blue]Clear RV REPL Screen[/bold blue]                ┃","Yellow")
    colorlib.cprint("┃     [bold yellow].show[/bold yellow]     [bold blue]Show stored code[/bold blue]                    ┃","Yellow")
    colorlib.cprint("┃                                                   ┃","Yellow")
    colorlib.cprint("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛","Yellow")

def abouts():
    colorlib.cprint(r"""
----------------------------------------------------------------------
 ______     __   ____          _        ____                          
|  _ \ \   / /  / ___|___   __| | ___  |  _ \ __ _ _ __ ___  ___ _ __ 
| |_) \ \ / /  | |   / _ \ / _` |/ _ \ | |_) / _` | '__/ __|/ _ \ '__|
|  _ < \ V /   | |__| (_) | (_| |  __/ |  __/ (_| | |  \__ \  __/ |   
|_| \_\ \_/     \____\___/ \__,_|\___| |_|   \__,_|_|  |___/\___|_|                                   
                                                                      
----------------------------------------------------------------------
Copyright © 2019-${year} StarWorld 
        """.replace("${year}",str(datetime.datetime.now().date().year)),"Yellow")



prototype = {
    "window":{
        "title":"RV",
        "version":version,
        "platform":platform.uname(),
        "resolution":os.get_terminal_size,
    },
    "document":{
        "write":sys.stdout.write,
        "clear":colorlib.consoles.clear,
        "#document":colorlib.consoles,
    },
    "print":print,
    "system":os.system,
    "about":abouts,
    "help":helps,
    "__pyimport__":__import__,
    "__python__":eval,
    "dir":dir,
    "modules":sys.modules,
    "__builtins__":__builtins__,
    "__pyexec__":exec,
    "iostream":{
        "input":input,
        "output":print,
        "raw_input":sys.stdin,
        "raw_output":sys.stdout,
    },
    "fopen":open,
    "pass":lambda *args,**kwargs:None,
    "range":lambda start,stop=0,step=1:list(range(int(str(start).replace("'","")),int(str(stop).replace("'","")),int(str(step).replace("'","")))),
    "XMLHttpRequest":{
        "get":lambda url,data,headers:requests.get(url=str(url).replace("'",""),data=data,headers=headers),
        "post":lambda url,data,headers:requests.post(url=str(url).replace("'",""),data=data,headers=headers),
    },
    "setTimeout":lambda function,second:[sleep(float(str(second).replace("'",""))),function()],
    "getAttributes":getAttributes,
}

