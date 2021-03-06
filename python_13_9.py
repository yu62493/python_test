# _*_ coding: utf-8 _*_

from  PIL import Image, ImageDraw
im = Image.open('test.jpg')
w, h = im.size
dw = ImageDraw.Draw(im)
dw.line((0,0,w,h), width=20, fill=(255,0,0))
dw.line((w,0,0,h), width=20, fill=(255,0,0))
dw.ellipse((50,50,w-50,h-50),outline=(255,255,0))
dw.text((100,100), 'This is a test image')
im.show()

