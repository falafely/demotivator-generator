from PIL import Image, ImageDraw, ImageFont

demotivator = Image.new('RGB', (1000, 1000), color='black')
draw = ImageDraw.Draw(demotivator)
draw.rectangle((170, 170, 830, 830), fill='black', outline=(255, 255, 255), width=3)

photo = Image.open('your_pict.png')  # your_pict.png - ваше изображение
resize_photo = photo.resize((600, 600))

new_x, new_y = resize_photo.size
bs_x, bs_y = demotivator.size

a = (bs_x - new_x) // 2
b = (bs_y - new_y) // 2
demotivator.paste(resize_photo, (a, b))

text = 'example'

font = ImageFont.truetype('/usr/share/fonts/TTF/AkaashNormal.ttf', size=50)  # заменить шрифт на свой

text_width, text_height = draw.textsize(text, font=font)
x = (demotivator.width - text_width) // 2
y = 900

draw.text((x, y), text, font=font, fill=(255, 255, 255))  # выставить свои координаты

demotivator.show()
demotivator.save('demotivator.png')