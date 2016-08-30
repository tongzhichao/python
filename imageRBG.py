from PIL import Image,ImageDraw,ImageFont,ImageFilter
import  random

#随机ASCII字符在65到90之间的字母
def rndChar():
	return chr(random.randint(65,90))
#随机生成一种颜色(67,67,67)
def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#设置长,高
width = 240
height = 60 

#创建图片，背景为(100,100,100)
image = Image.new('RGB',(width,height),(100,100,100))
#生成一种字体对象
font=ImageFont.truetype('/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf',36)
#生成画图对象
draw = ImageDraw.Draw(image)
#遍历图片的每个点，生成背景
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())
#以60倍间距生成字母，字体为font，背景为rndColor2
for  t in range(4):
	draw.text((t*60,10),rndChar(),font=font,fill=rndColor2())
#图片模糊化处理
image = image.filter(ImageFilter.BLUR)
image.save('tong1.jpg','jpeg')
