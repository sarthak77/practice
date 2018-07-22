from PIL import ImageFont,Image,ImageDraw
a=Image.new('RGBA',(200,200),'white')
draw=ImageDraw.Draw(a)
x=ImageFont.truetype('/usr/share/fonts/nanum/NanumBarunGothicBold.ttf',32)
draw.text((20, 150), 'Hello', fill='purple',font=x)
a.save('sample.png')
