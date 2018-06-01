import pytesseract
from PIL import Image

image = Image.open('4.png')
code = pytesseract.image_to_string(image)
print(code)

