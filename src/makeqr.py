import os
import segno
import matplotlib.pyplot as plt
import matplotlib.image as img

def makeqrcode(content, name, scale):
    qrcode = segno.make_qr(content)
    path = name + ".png"
    qrcode.save(path, scale=scale)
    current_dir = os.getcwd()
    imgpath = current_dir + "/" + path
    image = img.imread(imgpath)
    plt.imshow(image)
    plt.show()
    print("qr code saved in " + current_dir)