from PIL import Image
a=Image.open('zophie.png')
width,height=a.size
b=a.resize((int(width/2),int(height/2)))
b.save('resize.png')