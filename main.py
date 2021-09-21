#vars
path = "W:\pelis"
i = 0
HTML = "<table>"

#Python Libraries
import os
import pathlib

def saveInfo(HTML):
	newPath = path+"\index.htm"
	print ("Saving info in "+newPath)
	f = open(newPath,'w')
	f.write(HTML)
	f.close
	
def defName(link):
	return link[link.rfind("/")+1:]

allFiles = os.listdir(path)

for folder in pathlib.Path(path).iterdir():   # search all directories in path 
	if folder.is_dir():
		subdir = folder.name
		HTML += ("<TR><th colspan=2><b>"+subdir+"</th></tr>")
		subfolder = pathlib.Path(path+"\\"+subdir)
		for filePath in (subfolder).iterdir():       # search files in folders. Note that its a 'pathlib.WindowsPath' class
			i += 1
			prepareLink = str(filePath).replace("\\", "/")
			link = prepareLink.replace("W:/pelis/", "http://neconas.synology.me/pelis")
			name = defName(link)
			HTML += ("<tr><th>"+str(i)+"</th><td><a href='"+link +"'>"+str(name)+"</a></td></tr>")
			# file = str(filePath)
			# print (file)
HTML += "</TABLE>"
saveInfo(HTML)