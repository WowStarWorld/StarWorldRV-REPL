import os,sys,colorlib,platform,requests
import datetime
import func
from time import sleep


version = "7.1.1"
def getAttributes(obj):
    attrs_dict = {}
    try:
        for i in range(len(dir(obj))-1):    
                if not dir(obj)[i].startswith("__") and dir(obj)[i] != "this" and dir(obj)[i] != "self" and dir(obj)[i] != "value":
                    attrs_dict[dir(obj)[i]] = [getattr(obj,dir(obj)[i])]
    except:pass
    return attrs_dict

    
fopen = open
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
                                                                      
 ______     __  ____                _   _____            _             _         ____       _       _     _                      
|  _ \ \   / / |  _ \ ___  __ _  __| | | ____|_   ____ _| |_   _  __ _| |_ ___  |  _ \ _ __(_)_ __ | |_  | |    ___   ___  _ __  
| |_) \ \ / /  | |_) / _ \/ _` |/ _` | |  _| \ \ / / _` | | | | |/ _` | __/ _ \ | |_) | '__| | '_ \| __| | |   / _ \ / _ \| '_ \ 
|  _ < \ V /   |  _ <  __/ (_| | (_| | | |___ \ V / (_| | | |_| | (_| | ||  __/ |  __/| |  | | | | | |_  | |__| (_) | (_) | |_) |
|_| \_\ \_/    |_| \_\___|\__,_|\__,_| |_____| \_/ \__,_|_|\__,_|\__,_|\__\___| |_|   |_|  |_|_| |_|\__| |_____\___/ \___/| .__/ 
                                                                                                                          |_|    

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
    "sys":{
        "ps1":">",
        "ps2":"...",
    },
    "system":os.system,
    "about":abouts,
    "help":helps,
    "__pyimport__":__import__,
    "__python__":eval,
    "dir":dir,
    "modules":sys.modules,
    "__builtins__":__builtins__,
    "__pyexec__":exec,
    "chr":lambda x:chr(int(str(x).replace("'",""))),
    "ord":lambda x:ord(str(x.to_string())[1]),
    "iostream":{
        "input":input,
        "output":print,
        "raw_input":sys.stdin,
        "raw_output":sys.stdout,
    },
    "pass":lambda *args,**kwargs:None,
    "fopen":fopen,
    "range":lambda start,stop=0,step=1:list(range(int(str(start).replace("'","")),int(str(stop).replace("'","")),int(str(step).replace("'","")))),
    "XMLHttpRequest":{
        "get":lambda url,data,headers:requests.get(url=str(url).replace("'",""),data=data,headers=headers),
        "post":lambda url,data,headers:requests.post(url=str(url).replace("'",""),data=data,headers=headers),
    },
    "setTimeout":lambda function,second:[sleep(float(str(second).replace("'",""))),function()],
    "getAttributes":getAttributes,
    "$":func.selector,
}
