from PIL import Image
x=Image.open('zophie.png')
y=x.crop((335,345,565,560))#box tupple
y.save('cropped.png')