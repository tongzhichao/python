from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def writer_number(image_file_path,number=1):
	img = Image.open('blur.jpg')
	print('the image\'s weight: %d' % img.size[0])
	print('the image\'s hight: %d' %  img.size[1])

	font_size = img.size[0] if img.size[0] < img.size[1] else img.size[1]
	print('the small to font_size:%d ' % font_size)
	font_size = font_size // 4
	print('the font_size %d' % font_size)
	number_txt = str(number) + ' ' if number < 100 else '99+'
	print(number_txt)
	print(isinstance(number_txt,str))
	#加载字体格式和字体大小
	font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf",size=font_size)
	#font为返回的字体的对象，为元组类，打印[0]看看
	print(font.getsize(number_txt)[0])	
	if font.getsize(number_txt)[0] > img.size[0] or font.getsize(number_txt)[1] > img.size[1]:
		return img
	position = img.size[0] - font.getsize(number_txt)[0]
	ImageDraw.Draw(img).text((position,0),number_txt,(255,0,0),font)
	return img

writer_number('000.png').save('result.png')
#writer_number('0000.png',100).save('result100.png')
