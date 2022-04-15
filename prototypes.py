import os,sys,colorlib,platform,requests,json



version = "6.9.3"


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
Copyright © 2019-2021 StarWorld 
        ""","Yellow")


prototype = {
    "window":{
        "title":"RV",
        "version":version,
        "platform":platform.uname(),
        "resolution":os.get_terminal_size,
    },
    "print":print,
    "system":os.system,
    "about":abouts,
    "help":helps,
    "locals":locals,
    "colorlib":colorlib,
    "__pyimport__":__import__,
    "__python__":eval,
    "__pyexec__":exec,
    "iostream":{
        "input":input,
        "output":print,
        "raw_input":sys.stdin,
        "raw_output":sys.stdout,
    },
    "fstream":{
        "fopen":open,
    },
    "wrapper":{
        "dir":dir,
        "type":type,
        "Exception":Exception,
        "BaseException":BaseException,
        "pass":None,
        "platform":platform,
        "json_parser":json,
        "chr":chr,
        "ord":ord,
        "os":os,
        "sys":sys,
        "range":range,
    },
    "XMLHttpRequest":{
        "get":requests.get,
        "post":requests.post,
        "wrapper":requests,
    },
}

