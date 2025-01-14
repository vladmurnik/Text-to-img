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

def decip_2(name,coords,size):
    im = Image.open(name)
    rgb_im = im.convert('RGB')
    rgb_im = rgb_im.crop((coords[0],coords[1],size+coords[0],size+coords[1]))
    rgb_im.save('result2.png')
    rgb_im = Image.open('result2.png')
    color = rgb_im.getcolors()
    x, y = rgb_im.size
    stri = []
    for q in range(x):
        for w in range(y):
            pix = rgb_im.getpixel((w, q))
            if pix != (0,0,0):
                for i in pix:
                    if i != 0:
                        stri.append(i)

    def prove(stri):
        for i in stri:
            if i == 43:
                return True
            if i == 45:
                return True
            if i == 42:
                return True
            if i == 47:
                return True
        else:
            return False
    while prove(stri) == True:
        for num,i in enumerate(stri):
            try:
                if stri[num] == 43:
                    mas = [stri[num-1],stri[num+1]]
                    stri.pop(num+1)
                    stri[num] = mas[0] + mas[1]
                    stri.pop(num-1)
                    print(mas[0] + mas[1])
                if stri[num] == 45:
                    mas = [stri[num-1],stri[num+1]]
                    stri.pop(num+1)
                    stri[num] = mas[0] - mas[1]
                    stri.pop(num-1)
                    print(mas[0] - mas[1])
                if stri[num] == 42:
                    mas = [stri[num-1],stri[num+1]]
                    stri.pop(num+1)
                    stri[num] = mas[0] * mas[1]
                    stri.pop(num-1)
                    print(mas[0] * mas[1])
                if stri[num] == 47:
                    mas = [stri[num-1],stri[num+1]]
                    stri.pop(num+1)
                    stri[num] = mas[0] / mas[1]
                    stri.pop(num-1)
                    print(mas[0] / mas[1])
            except IndexError:
                pass
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
name_img = input('Name you img:')
in_img_y_or_n = input('Insert into photo?')
if in_img_y_or_n == 'y':
    x = int(input('X:'))
    y = int(input('Y:'))
    coords = [x,y]
    in_img(name_img,'result.png','img_result.png',coords)
    print(decip('result.png',coords,a))
else:
    coords = [0,0]
    print(decip('result.png',coords,a))
