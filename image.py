from PIL import Image, ImageDraw, ImageFont
import api
import textwrap
def prepare_image():
    img = Image.open("chuck.jpg",'r')
    width_img, height_img = img.size
    imgdraw = ImageDraw.Draw(img)
    text=api.apicall()
    lines = textwrap.wrap(text, width=40)
    y_text = 100
    y_text = (height_img - y_text)/2
    font= ImageFont.truetype("JosefinSans-SemiBold.ttf", size=30)

    for line in lines:
        width, height = font.getsize(line)
        imgdraw.text(((width_img - width) / 2, y_text), line, font=font, fill="white",shadow=(1.0,1.0),width=60,align="center")
        y_text += height
    img.save("image.png")