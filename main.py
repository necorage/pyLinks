#Python Libraries (import)
import os
import pathlib

# Create All vars i will need, including HTML with headings
path = "W:\pelis"
i = 0

HTML = """
<!DOCTYPE html>
<html>
<body>

<h1>PELIS NECONAS ;)</h1>
<table>
"""
allFiles = os.listdir(path)

# in this function I take all content in HTML var and I insert in the index file
def saveInfo(HTML):
	newPath = path+"\index.htm"
	print ("Saving info in "+newPath)
	f = open(newPath,'w')
	f.write(HTML)
	f.close

# This function takes the complete link and give me only the name (with / to use in the link) 
def defName(link):
	return link[link.rfind("/"):]

# Here really starts "the main" program
for folder in pathlib.Path(path).iterdir():   # search all directories in path 
	if folder.is_dir():  # if this is a directory, save the name to search inside
		subdir = folder.name 
		HTML += ("<TR><th colspan=2><b>"+subdir+"</TH></TR>") # I use this name to the heading in the list
		subfolder = pathlib.Path(path+"\\"+subdir)
		for filePath in (subfolder).iterdir():       # search files in folders. Note that its a 'pathlib.WindowsPath' class
			i += 1
			prepareLink = str(filePath).replace("\\", "/")
			link = prepareLink.replace("W:/pelis/", "http://neconas.synology.me/pelis/")
			name = defName(link).replace("/","")
			HTML += ("<TR><TH>"+str(i)+"</TH><TD><A href='"+link +"'>"+str(name)+"</A></TD></TR>")
			# file = str(filePath)
			# print (file)
HTML += """
</body>
</html>
</TABLE>"""
saveInfo(HTML)