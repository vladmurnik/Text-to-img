from PIL import Image
import math
def cip(stri):
    sz = math.ceil(len(stri)/3)
    im = Image.new("RGB", (sz, 1))
    rgb_im = im.convert('RGB')
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
            pixels[i, j] = list_2[(10 * j) + i][0],list_2[(10 * j) + i][1],list_2[(10 * j) + i][2], 255
    im.save('orig.png')

def decip(name):
    im = Image.open(name)
    rgb_im = im.convert('RGB')
    color = rgb_im.getcolors()
    x, y = im.size
    stri = ''
    for q in range(x):
        for w in range(y):
            pix = rgb_im.getpixel((q, w))
            if pix != (0,0,0):
                for i in pix:
                    if i != 0:
                        stri += chr(i)
    return(stri)
