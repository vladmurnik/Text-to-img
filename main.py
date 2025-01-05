from PIL import Image
import math
import os
def glcip(stri,name):

    def cip(stri, name):
        sz = math.ceil(len(stri)/3)
        im = Image.new("RGBA", (sz, 1))
        rgb_im = im.convert('RGBA')
        color = rgb_im.getcolors()
        pixels = im.load()
        x, y = im.size

        list = [stri[i:i + 3] for i in range(0, len(stri), 3)]
        list_2 = []
        for i in list:
            stro = []
            for a in i:
                stro.append(ord(a))
            list_2.append(stro)
        if len(list_2[-1]) == 2:
            l = list_2[-1]
            l.append(0)
            list_2[-1] = l
        if len(list_2[-1]) == 1:
            l = list_2[-1]
            l.append(0)
            l.append(0)
            list_2[-1] = l
        for i in range(sz * sz - len(list_2)):
            list_2.append([0,0,0])
        for i in range(x):
            for j in range(y):
                pixels[i, j] = list_2[i][0],list_2[i][1],list_2[i][2], 255
        im.save(name)
    if len(stri) > a*3:
        im = Image.new("RGBA", (a, a))
        im.save('result.png')
        stri = [stri[i:i + a*3] for i in range(0, len(stri), a*3)]
        for num,i in enumerate(stri):
            cip(i,str(num)+name)
            im1 = Image.open(str(num)+name)
            im2 = Image.open('result.png')
            back_im = im2.copy()
            back_im.paste(im1,(0,num))
            back_im.save('result.png')
            os.remove(str(num)+name)
    else:
        cip(stri,'result.png')
def decip(name,coords,size):
    im = Image.open(name)
    rgb_im = im.convert('RGB')
    rgb_im = rgb_im.crop((coords[0],coords[1],size+coords[0],size+coords[1]))
    rgb_im.save('result2.png')
    rgb_im = Image.open('result2.png')
    color = rgb_im.getcolors()
    x, y = rgb_im.size
    stri = ''
    for q in range(x):
        for w in range(y):
            pix = rgb_im.getpixel((w, q))
            if pix != (0,0,0):
                for i in pix:
                    if i != 0:
                        stri += chr(i)
    return(stri)

def in_img(name1,name2,name3,coord):
    im1 = Image.open(name1)
    im2 = Image.open(name2)
    back_im = im1.copy()
    back_im.paste(im2,coord)
    back_im.save(name3)
    im1.close()
    im2.close()

stri = input('Text:')
name = 'orig.png'
a = 0
while a*a*3 < len(stri):
    a += 1
glcip(stri,name)
x = int(input('X:'))
y = int(input('Y:'))
coords = [x,y]
name_img = input('Name you img:')
in_img(name_img,'result.png','img_result.png',coords)
print(decip('img_result.png',coords,a))
