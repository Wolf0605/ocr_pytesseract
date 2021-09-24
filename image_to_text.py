import pytesseract
import pytesseract as tess
pytesseract.pytesseract.tesseract_cmd = r'E:\tesseract\tesseract.exe'

from PIL import Image

img1 = Image.open('Resources/kor_menu2.jpg')
# img2 = Image.open('Resources/eng_menu1.jpg')
# img3 = Image.open('Resources/jpn_menu1.jpg')
# Image._show(img)
text1 = pytesseract.image_to_string(img1, lang='kor')
# text2 = pytesseract.image_to_string(img2)
# text3 = pytesseract.image_to_string(img3, lang='jpn')
print(text1)
print("="*50)
# print(text2)
# print("="*50)
# print(text3)
