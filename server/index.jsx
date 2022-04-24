<?RV

print("<!DOCTYPE HTML>\n<html>\n<head>\n<title>index of "+path+"</title>")

print("\n<link href=\"https://cdn.staticfile.org/twitter-bootstrap/5.1.1/css/bootstrap.min.css\" rel=\"stylesheet\">\n<script src=\"https://cdn.staticfile.org/twitter-bootstrap/5.1.1/js/bootstrap.bundle.min.js\"></script>")
print("\n</head>\n<body>\n<br/>")
print("<div class=container>\n<h1>Index of "+path+"</h1>\n<hr/>\n")
print("<ul class=\"list-group\">")
files = __pyimport__('os').listdir()
var i;
let blackfile = ["index.jsx","server.json"]
for (i = 0; i < files.length; i++) {
  if (blackfile.indexOf(files[i]) == -1) {
    print("<li class=\"list-group-item\"><a href=\""+files[i]+"\" data-toggle=tooltip data-placement=top title=\""+files[i]+"\"><h4>"+files[i]+"</h4></a></li>");
  }
}
print("</ul>\n</div>\n</body>\n</html>")

?>