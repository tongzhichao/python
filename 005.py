#http://www.jb51.net/article/59893.htm
import glob,os
from PIL import Image

def change_image_size(size):
	for infile in glob.glob(r"/home/tzc/*.jpg"):
		files,ext = os.path.splitext(infile)
#		print(files)
#		print(ext)
		img = Image.open(infile)
		x,y = img.size

		changex = float(x) / size[0]
		changey = float(y) / size[1]
		if  changex > 1 or changey > 1:
			change = changex  if changex > changey else changey
			img.resize((int(x /change),int(y/change))).save(files+'.thumbnail','JPEG')

	

change_image_size((1136,640))

