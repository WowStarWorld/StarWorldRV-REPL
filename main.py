import os,sys
from js2py.internals.simplex import JsException
from js2py.pyjs import builtins as jsbuiltins
import platform
import json
import js2py
import requests
import prototypes
import colorlib
import threading
from rich import syntax
import readline

version = prototypes.version
argv = sys.argv
keywords = ["pyimport","break","case","catch","const","delete","else","enum","eval","extends","finally","for","function","if","in","instanceof","let","new","return","super","switch","throw","try","typeof","var","void","while","with","yield"]
def res_dis(file,fl=__file__):
    ic = os.path.split(os.path.realpath(fl))[ 0 ]+"/"+file
    return ic.replace("\\","/")
class function:
    def include(url):
        try:
            context.execute(requests.get(str(url).replace("'","")).content.decode('utf-8'))
            return {
                "no_error":True,
                "error_name":"Not Found",
                "error_message":"Not Found",
                "error":Exception("Not Found"),
            }
        except BaseException as e:
            return {
                "no_error":False,
                "error_name":e.__class__.__name__,
                "error_message":str(e),
                "error":e,
            }

class rv:
    global prototypes
    def libs():
        liblist = []
        if os.path.exists(res_dis("libs")):
            if os.path.exists(res_dis("libs/site-packages/")):
                listpl = os.listdir(res_dis("libs/site-packages/"))
                for i in range(len(listpl)):
                    if os.path.isfile(res_dis("libs/site-packages/"+listpl[i])):
                        if os.path.splitext(res_dis("libs/site-packages/"+listpl[i]))[1] in [".js","rv"]:
                            with open(res_dis("libs/site-packages/"+listpl[i]),"rb") as f:
                                try:
                                    execute = lambda:context.execute(f.read().decode("UTF-8"))
                                    thread = threading.Thread(target=execute)
                                    thread.start()
                                    liblist.append(listpl[i])
                                except BaseException:
                                    try:
                                        colorlib.cprint("\nFail to load lib "+str(listpl[i])+f": {sys.exc_info()[1]}","Red")
                                    except:
                                        pass
                                    continue

                    i = i + 1
            else:
                os.mkdir(res_dis("libs/site-packages"))

        else:
            os.mkdir(res_dis("libs"))
        return liblist
    def stdlibs():
        liblist = []
        if os.path.exists(res_dis("libs/")):
            listpl = os.listdir(res_dis("libs/"))
            for i in range(len(listpl)):
                if os.path.isfile(res_dis("libs/"+listpl[i])):
                    if os.path.splitext(res_dis("libs/"+listpl[i]))[1] in [".jsx","rvx"]:
                        with open(res_dis("libs/"+listpl[i]),"rb") as f:
                            try:
                                execute = lambda:context.execute(f.read().decode("UTF-8"))
                                thread = threading.Thread(target=execute)
                                thread.start()
                                liblist.append(listpl[i])
                            except BaseException:
                                try:
                                    colorlib.cprint("\nFail to load lib "+str(listpl[i])+f": {sys.exc_info()[1]}","Red")
                                except:
                                    pass
                                continue
                    elif os.path.splitext(res_dis("libs/"+listpl[i]))[1] in [".py",".pyw",".pyi"]:
                        with open(res_dis("libs/"+listpl[i]),"rb") as f:
                            try:
                                execute = lambda:exec(f.read().decode("UTF-8"))
                                thread = threading.Thread(target=execute)
                                thread.start()
                                liblist.append(listpl[i])
                            except BaseException:
                                try:
                                    colorlib.cprint("\nFail to load lib "+str(listpl[i])+f": {sys.exc_info()[1]}","Red")
                                except:
                                    pass
                                continue
                i = i + 1
        else:
            os.mkdir(res_dis("libs"))
        return liblist


def run(code):
    global loads
    global temps
    if code == ".about":
        prototypes.abouts()
    elif code == ".help":
        prototypes.helps()
    elif code == ".exit":
        sys.exit(0)
    elif code == ".cls":
        colorlib.consoles.clear()
        colorlib.cprint(f"RV v{version} on {platform.platform()}","Yellow")
        colorlib.cprint(f'Type ".help" or ".about" for more information.',"Bold Blue")
    elif code == ".debug":
        try:
            colorlib.cprint(json.dumps(js2py.parse_js(loads),indent=2),"grey")
        except:
            colorlib.cprint(sys.exc_info()[1],"Red")
            colorlib.cprint("Error Code:","red")
            colorlib.cprint(loads,"yellow")
    elif code == ".editor":
        colorlib.consoles.clear()
        colorlib.cprint("~[/blue] // Entering editor mode (^D to finish, ^C to cancel)[blue] ","Blue")
        cms = "// Entering editor mode (^D to finish, ^C to cancel)\n"
        while True:
            try:
                
                command = colorlib.cinput("~ ","blue")
                if command == "\x04":
                    loads = cms
                    break
                else:
                    cms = cms + "\n" +command
            except KeyboardInterrupt:
                break
            except EOFError:
                loads = cms
                break
        colorlib.consoles.clear()
        colorlib.cprint(f"RV v{version} on {platform.platform()}","Yellow")
        colorlib.cprint(f'Type ".help" or ".about" for more information.',"Bold Blue")
        

    elif code == ".load":
        try:
            context.execute(loads)
        except:
            if sys.exc_info()[0] != JsException:
                info = str(sys.exc_info()[0].__name__) +":"+ str(sys.exc_info()[1])
            else:
                info = str(sys.exc_info()[1])
            colorlib.cprint(info,"Red")
            colorlib.cprint("Error Code:","red")
            colorlib.cprint(loads,"yellow")
    elif code == ".clear":
        loads = ""
    elif code == ".show":
        colorlib.consoles.print(syntax.Syntax(loads, "javascript", theme="vim", line_numbers=True))
        
    elif len(code) >=1 and code[0] == ".":
        colorlib.cprint("Invalid REPL Command","Red")
    else:
        loads = loads + "\n" + code 
        try:
            __par__ = context.eval(code)
            if str(__par__) == "None":
                colorlib.cprint("undefined",color="bold black")
            else:
                colorlib.cprint(__par__,"gray")
        except:
            if "{" in code:
                temps += str(code).count("{")
            if "}" in code:
                if temps >= str(code).count("}"):
                    temps -= str(code).count("}")
            elif "{" not in code and "}" and ":" not in code and "return" not in code:
                if str(sys.exc_info()[1]) != "":
                    colorlib.cprint(str(sys.exc_info()[0].__name__) +":"+ str(sys.exc_info()[1]) if sys.exc_info()[0] != JsException else str(sys.exc_info()[1]),"Red")
                else:
                    colorlib.cprint(str(sys.exc_info()[0].__name__) if str(sys.exc_info()[0]) != JsException else str(sys.exc_info()[1]),"Red")
prototypes.prototype["include"] = function.include
prototypes.prototype["reload_modules"] = lambda: {"site-packages":rv.libs(),"standard-packages":rv.stdlibs()}

context = js2py.EvalJs(prototypes.prototype)
loads = ""
temps = 0
try:
    rv.libs()
    rv.stdlibs()
except:
    pass

raw_input = lambda prompt:input(prompt if temps==0 else "..."*temps+" ")

CMDLocals = list(context.eval("Object.keys(this)")) + list(jsbuiltins) + keywords
CMDLocals.remove("this")
CMD = CMDLocals
def completer(text, state):
    options = [cmd for cmd in CMD if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None
readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

if __name__ == "__main__":
    if len(argv) == 1:
        colorlib.consoles.clear()
        colorlib.cprint(f"RV v{version} on {platform.platform()}","Bold Yellow")
        colorlib.cprint(f'Type ".help" or ".about" for more information.',"Bold Blue")
        try:
            rv.libs()
            rv.stdlibs()
        except:
            pass
        while True:
            try:
                code = raw_input("> ")
                run(code)
                CMDLocals = list(context.eval("Object.keys(this)")) + list(jsbuiltins) + keywords
                CMDLocals.remove("this")
                CMD = CMDLocals
            except KeyboardInterrupt:
                colorlib.cprint("KeyboardInterrupt","Red")
                break
            except EOFError:
                print("\n")
            except RuntimeError:
                pass
        sys.exit(0) 
    elif len(argv) == 2:
        try:
            try:
                rv.libs()
                rv.stdlibs()
            except:
                pass
            with open(argv[1],"rb") as f:
                codes = f.read().decode("utf-8")
                context.execute(codes)
        except:
            colorlib.cprint(sys.exc_info()[1],"Red")
    elif len(argv) == 3:
        try:
            try:
                rv.libs()
                rv.stdlibs()
            except:
                pass
            if argv[1] != "#temp" :
                with open(argv[1],"rb") as f:
                    codes = f.read().decode("utf-8")
                    context.execute(codes)
            run(argv[2])
        except:
            colorlib.cprint(sys.exc_info()[1],"Red")