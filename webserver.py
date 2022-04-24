from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sys
import json
import main
context = main.context
import os

jsfile = ""
header = [["Content-type","text/html"]]
data = ""
fl = ""

        
def run(self,files):
    global fl
    fl = ""
    readmode = 0
    try:
        file = self.example()+open(files,"rb").read().decode("utf-8")
    except UnicodeDecodeError:
        file = open(files,"rb").read()
        self.wfile.write(file)
        readmode = 1
    head = 0
    try:
        if readmode == 0:
            files = file.replace("\r","").split("\n")
            for i in range(len(files)):
                if files[i].lstrip().rstrip() == "<?RV":
                    head = 1
                elif files[i].lstrip().rstrip() == "?>":
                    head = 0
                    context.execute(fl)
                    #fl = ""
                elif head == 0:
                    print(files[i])
                elif head == 1:
                    fl = fl + files[i] + "\n"
                i = i + 1
    except BaseException as e:
        print(e)
        pass
class stdout:
    def write(string):
        global data
        data = data + string
    def flush(*args):
        pass

class errors:
    e404 = b"""\n    <html>\n    <head>\n    <title>404 Not Found</title>\n    <link rel=\"stylesheet\" href=\"https://cdn.staticfile.org/twitter-bootstrap/5.1.1/css/bootstrap.min.css\">\n    <script src=\"https://cdn.staticfile.org/popper.js/2.9.3/umd/popper.min.js\"></script>\n    <script src=\"https://cdn.staticfile.org/twitter-bootstrap/5.1.1/js/bootstrap.min.js\"></script>\n    </head>\n    <body style="display: -webkit-box;display: flex;-webkit-box-orient: horizontal;-webkit-box-direction: normal;flex-flow: row wrap;align-content: center;-webkit-box-pack: center;justify-content: center;">\n    <br/><br/>\n    <center>\n    <div class=container>\n    <h1 class="text-warning">404 Not Found</h1>\n    <hr>\n    <h4 class="text-primary">RV</h4>\n    <br/><br/><br/>\n    <div class="btn-group" role="group" aria-label="Basic outlined example">\n        <button type="button" class="btn btn-outline-success" onclick="history.back();">Back</button>\n        <button type="button" class="btn btn-outline-success" onclick="location.reload();">Reload</button>\n        <button type="button" class="btn btn-outline-success" onclick="location='/';">Home</button>\n    </div>\n    </div>\n    </center>\n    </body>\n    </html>\n    """
host = ('localhost', 9999) 
class Resquest(BaseHTTPRequestHandler):
    def example(self):
        example = f"""
<?RV
path = "{self.path}";
?>
"""+"\n" 
        return example
    def do_GET(self):
        global data
        data = ""
        self.send_response(200)
        i = 0
        for i in range(len(header)-1):
            self.send_header(header[i][0], header[i][1])
            i = i + 1
        self.end_headers()
        main.rv.libs()
        main.rv.stdlibs()
        if self.path == "/" or self.path.split("?")[0] == "/":
            try:
                run(self,jsfile)
            except BaseException as e:
                print(e)
                pass
            self.wfile.write(data.encode("utf-8"))
        elif os.path.splitext("."+self.path.split("?")[0])[-1] in [".sws",".sw",".jsi",".jsx",".swi"]:
            try:
                main.rv.libs()
                main.rv.stdlibs()
            except BaseException as e:
                print(e)
                pass
            try:
                run(self,"."+self.path.split("?")[0])
            except FileNotFoundError:
                self.wfile.write(errors.e404)
            self.wfile.write(data.encode("utf-8"))
        else:
            try:
                run(self,"."+self.path.split("?")[0])
                pass
            except:
                if True:
                    try:
                        run(self,"."+self.path.split("?")[0]+".jsx")
                    except FileNotFoundError:
                        try:
                            run(self,"."+self.path.split("?")[0]+"index.jsx")
                        except FileNotFoundError:
                            try:
                                try:
                                    run(self,"."+str(self.path.split("?")[0]))
                                except FileNotFoundError:
                                    run(self,"."+self.path.split("?")[0]+"/index.jsx")
                                except PermissionError:
                                    run(self,"."+self.path.split("?")[0]+"/index.jsx")
                            except FileNotFoundError:
                                self.wfile.write(errors.e404)
                    self.wfile.write(data.encode("utf-8"))
                pass
                
        

if __name__ == '__main__':
    os.chdir(main.res_dis("server"))
    argv = json.loads(open(main.res_dis("server/server.json")).read())
    jsfile = argv["javascript"]
    header = argv["headers"]
    host = (argv["ip"],int(argv["port"]))
    errors.e404 = str(argv["errors"]["404"]).encode("utf-8")
    print(f"The server started on {host[0]}:{host[1]}")
    sys.stdout = stdout
    server = HTTPServer(host, Resquest)
    server.serve_forever()
