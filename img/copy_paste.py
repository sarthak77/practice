from PIL import Image
a=Image.open('zophie.png')
b=a.copy()
b.save('copy.png')
face = a.crop((335, 345, 565, 560))
b.paste(face,(0,0))
b.paste(face,(400,500))#coordinates of top left
b.save('paste.png')