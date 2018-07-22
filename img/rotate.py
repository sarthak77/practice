from PIL import Image
a=Image.open('zophie.png')
a.rotate(90).save('rotate.png')
a.rotate(100,expand=True).save('rotate2.png')

a.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
a.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')