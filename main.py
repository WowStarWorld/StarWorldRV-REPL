import os,sys
from js2py.internals.simplex import JsException
from js2py.pyjs import builtins as jsbuiltins
import json
import js2py
import requests
import prototypes
import colorlib
import threading
from rich import syntax
import readline
from prototypes import information
sys.stderr = lambda *args: None
version = prototypes.version
argv = sys.argv

keywords = ["pyimport","break","case","catch","const","delete","else","continue","enum","eval","extends","finally","for","function","if","in","instanceof","let","new","return","super","switch","throw","try","typeof","var","void","while","with","yield","debugger"]
js_exceptions = ["Error","ReferenceError","EvalError","URIError","SyntaxError","TypeError","RangeError"]
def res_dis(file,fl=__file__):
    ic = os.path.split(os.path.realpath(fl))[ 0 ]+"/"+file
    return ic.replace("\\","/")
class function:
    def include(url):
        try:
            context.execute(requests.get(str(url).replace("'","")).content.decode('utf-8'))
            return {
                "error":False,
                "error_name":"Not Found",
                "error_message":"Not Found",
                "error_type":Exception,
            }
        except BaseException as e:
            return {
                "error":True,
                "error_name":e.__class__.__name__,
                "error_message":str(e),
                "error_type":e.__class__,
            }
    def require(lib):
        try:
            context.execute(open(res_dis(str(lib).replace("'",""),str(context.eval("__file__")).replace("'","")),"rb").read().decode('utf-8'))
            return {
                "error":False,
                "error_name":"Not Found",
                "error_message":"Not Found",
                "error_type":Exception,
            }
        except BaseException as e:
            return {
                "error":True,
                "error_name":e.__class__.__name__,
                "error_message":str(e),
                "error_type":e.__class__,
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
                    if os.path.splitext(res_dis("libs/"+listpl[i]))[1] in [".jsx",".rvx"]:
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
    if code.strip().split(" ")[0] == ".about":
        prototypes.abouts()
    elif code.strip().split(" ")[0] == ".help":
        prototypes.helps()
    elif code.strip().split(" ")[0] == ".exit":
        sys.exit(0)
    elif code.strip().split(" ")[0] == ".cls":
        colorlib.consoles.clear()
        information()
    elif code.strip().split(" ")[0] == ".debug":
        try:
            colorlib.cprint(json.dumps(js2py.parse_js(loads),indent=2),"grey")
        except:
            colorlib.cprint(sys.exc_info()[1],"Red")
            colorlib.cprint("Error Code:","red")
            colorlib.consoles.print(syntax.Syntax(loads, "javascript", theme="vim", line_numbers=True))
    elif code.strip().split(" ")[0] == ".editor":
        colorlib.consoles.clear()
        colorlib.cprint("~[/blue] // Entering editor mode (^D to finish, ^C to cancel)[blue] ","Blue")
        cms = "// Entering editor mode (^D to finish, ^C to cancel)\n"
        while True:
            try:
                
                command = input("~ ")
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
        information()
        

    elif code.strip().split(" ")[0] == ".load":
        try:
            context.execute(loads)
        except:
            if sys.exc_info()[0] != JsException:
                info = str(sys.exc_info()[0].__name__) +":"+ str(sys.exc_info()[1])
            else:
                info = str(sys.exc_info()[1])
            colorlib.cprint(info,"Red")
            colorlib.cprint("Error Code:","red")
            colorlib.consoles.print(syntax.Syntax(loads, "javascript", theme="vim", line_numbers=True))
    elif code.strip().split(" ")[0] == ".clear":
        loads = ""
        temps = {"braces":0,"parentheses":0,"colon":0,"brackets":0}
    elif code.strip().split(" ")[0] == ".show":
        colorlib.consoles.print(syntax.Syntax(loads, "javascript", theme="vim", line_numbers=True))
        
    elif len(code) >=1 and code[0] == ".":
        colorlib.cprint("Invalid REPL Command","Red")
    else:
        if code != "\\!$stop-bs":
            loads = loads + "\n" + code 
        try:
            __par__ = context.eval(code)
            try:
                if __par__ == None:
                    colorlib.cprint("undefined","italic bold black")
                else:
                    colorlib.cprint(__par__,"aqua")
            except:
                colorlib.cprint(__par__,"aqua")
        except BaseException as e:
            if "{" in code:
                temps["braces"] = temps["braces"] + str(code).count("{")
            if "}" in code:
                if temps["braces"] >= str(code).count("}"):
                    temps["braces"] -= str(code).count("}")
                else:
                    raise SyntaxError("Cannot find ending sentence of opening sentence '}'")
            if "(" in code:
                temps["parentheses"] = temps["parentheses"] + str(code).count("(")
            if ")" in code:
                if temps["parentheses"] >= str(code).count(")"):
                    temps["parentheses"] -= str(code).count(")")
                else:
                    raise SyntaxError("Cannot find ending sentence of opening sentence ')'")
            if "[" in code:
                temps["brackets"] = temps["brackets"] + str(code).count("[")
            if "]" in code:
                if temps["brackets"] >= str(code).count("]"):
                    temps["brackets"] -= str(code).count("]")
                else:
                    raise SyntaxError("Cannot find ending sentence of opening sentence ']'")
            if code[len(code)-1] == ":":
                temps["colon"] += str(code).count(":")
            if code == "\\!$stop-bs":
                if temps["colon"] > 0:
                    temps["colon"] -= 1
            elif "{" not in code and "}" not in code and ":" not in code and "return" not in code and "(" not in code and ")" not in code and "[" not in code and "]" not in code and "," not in code:
                colorlib.cprint(str(sys.exc_info()[0].__name__) +": "+ str(sys.exc_info()[1]) if sys.exc_info()[0] != JsException else str(sys.exc_info()[1]),"Red")if str(sys.exc_info()[1]) != "" else colorlib.cprint(str(sys.exc_info()[0].__name__) if str(sys.exc_info()[0]) != JsException else str(sys.exc_info()[1]),"Red")
            elif "{" in code or "}" in code or "(" in code or ")" in code or "[" in code or "]" in code or ":" in code or "," in code:
                if "SyntaxError" in str(e) or "IndexError" in str(e):
                    pass
                else:
                    if str(sys.exc_info()[1]) != "":
                        colorlib.cprint(str(sys.exc_info()[0].__name__) +": "+ str(sys.exc_info()[1]) if sys.exc_info()[0] != JsException else str(sys.exc_info()[1]),"Red")
                    else:
                        colorlib.cprint(str(sys.exc_info()[0].__name__) if str(sys.exc_info()[0]) != JsException else str(sys.exc_info()[1]),"Red")
            
prototypes.prototype["include"] = function.include
prototypes.prototype["reload_modules"] = lambda: {"site-packages":rv.libs(),"standard-packages":rv.stdlibs(),"path":res_dis('')}
prototypes.prototype['argv'] = sys.argv
prototypes.prototype['require'] = function.require
prototypes.prototype['__file__'] = __file__
prototypes.prototype['__modulepath__'] = res_dis('')

context = js2py.EvalJs(prototypes.prototype)
loads = ""
temps = {"braces":0,"parentheses":0,"colon":0,"brackets":0}


rv.libs()
rv.stdlibs()


raw_input = lambda:input(str(context.eval("sys.ps1")+" ")  if (temps["braces"]+temps["parentheses"]+temps["brackets"]+temps["colon"])==0 else str(context.eval("sys.ps2"))*(temps["braces"]+temps["parentheses"]+temps["brackets"]+temps["colon"])+" ")

CMDLocals = list(context.eval("Object.keys(this)")) + list(jsbuiltins) + keywords + js_exceptions
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
        information()
        try:
            rv.libs()
            rv.stdlibs()
        except:
            pass
        while True:
            try:
                try:
                    code = raw_input()
                except:
                    sys.exit(0)
                if code == "":
                    run("\\!$stop-bs")
                elif code == "\\!$stop-bs":
                    run("SyntaxError(\"Unexpected token\")")
                else:
                    run(code)
                
                CMDLocals = list(context.eval("Object.keys(this)")) + list(jsbuiltins) + keywords + js_exceptions
                CMDLocals.remove("this")
                CMD = CMDLocals
            except KeyboardInterrupt:
                colorlib.cprint("KeyboardInterrupt","Red")
                break
            except EOFError:
                print("\n")
            except RuntimeError:
                pass
            except SyntaxError as e:
                if str(sys.exc_info()[1]) != "":
                    colorlib.cprint(str(sys.exc_info()[0].__name__) +": "+ str(sys.exc_info()[1]) if sys.exc_info()[0] != JsException else str(sys.exc_info()[1]),"Red")
                else:
                    colorlib.cprint(str(sys.exc_info()[0].__name__) if str(sys.exc_info()[0]) != JsException else str(sys.exc_info()[1]),"Red")
        sys.exit(0) 
    elif len(argv) >= 3:
        if (argv[1] == "--packages" or argv[1] == "-p"):
            import pip
            pip.main(argv[2:])
            sys.exit(0)
        try:
            try:
                rv.libs()
                rv.stdlibs()
            except:
                pass
            if argv[1] != "#temp" :
                with open(argv[1],"rb") as f:
                    codes = f.read().decode("utf-8")
                    context.execute(f"__file__=\"{argv[1]}\"\n{codes}")
            context.execute(argv[2])
        except:
            colorlib.cprint(sys.exc_info()[1],"Red")
    elif len(argv) > 1:
        
        if argv[1] == "--help" or argv[1] == "-h" or argv[1] == "/?":
            colorlib.cprint("Usage <*Command> [*Arguements]","Bold Yellow")
            colorlib.cprint("  --help[-h,/?]                : Show this help","Bold Yellow")
            colorlib.cprint("  --packages[-p] <args>        : Package Manager","Bold Yellow")
            colorlib.cprint("  (File/#temps) <*args> : Run RV File with *arguments","Bold Yellow")
            sys.exit(0)
        try:
            try:
                rv.libs()
                rv.stdlibs()
            except:
                pass
            with open(argv[1],"rb") as f:
                codes = f.read().decode("utf-8")
                
                context.execute(f"__file__=\"{argv[1]}\"\n{codes}")
        except:
            colorlib.cprint(sys.exc_info()[1],"Red")
