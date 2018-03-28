import os
import pytesseract
from PIL import Image
import os
import os.path
import re
import sys
import codecs

path ='C:\\Users\\think5\\PycharmProjects\\dongxu\\baoxian\\get_verify_pic\\pics'
files = os.listdir(path)

for i in range(0,len(files)):

    pic_path = path+'\\'+files[i]


    image = Image.open(pic_path)

    code = pytesseract.image_to_string(image)

    print(code)

    try:

        os.rename(pic_path, str(code)+'.png')

    except:

        next()