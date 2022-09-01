import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
from PIL import Image

mahesh = Image.open('textkalam.png')
text = tess.image_to_string(mahesh)

print(text)
