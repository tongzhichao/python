from PIL import Image,ImageDraw,ImageFont

def add_num(picpath,num):
	img = Image.open("image.jpg")
	x,y = img.size
	print(x,y)
	myfont=ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf",size=int(x //5))
	ImageDraw.Draw(img).text((int( x -(x//5)),0),str(num),font=myfont,fill='red')
	img.save('pic_with_num.jpg')
if __name__=='__main__':
	add_num('pic.jpg',9)
