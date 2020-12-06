ar fs = WScript.CreateObject("Scripting.FileSystemObject");
var file = fs.OpenTextFile("data.txt", 1);
var str = file.ReadLine();
var img = new Image();
img.src = str + '.png';
