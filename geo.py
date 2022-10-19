import ddddocr

ocr = ddddocr.DdddOcr()

# with open("E:\\tmp\\Captcha.jfif", 'rb') as f:
#     image = f.read()

# res = ocr.classification(image)
# print(res)



import io
 
import urllib.request
 
from PIL import Image
img_path = "https://www.poi86.com/Captcha?0.9167291555608337"
file = io.BytesIO(urllib.request.urlopen(img_path).read())
 
img = Image.open(file)


res = ocr.classification(img)
print(res)