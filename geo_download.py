
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By #导入By定位包


area_code_list = ["511002","511011","511024","511025","511083"]
webdriver.ChromeOptions()





dr=webdriver.ChromiumEdge()
for area_code in area_code_list:
    url = f"https://www.poi86.com/poi/download_area_geojson/{area_code}.html"
    dr.get(url)


    sleep(3)




    import base64
    import os
    import re
    from io import BytesIO
    from PIL import Image
    
    def base64_to_image(base64_str):
        base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
        byte_data = base64.b64decode(base64_data)
        image_data = BytesIO(byte_data)
        img = Image.open(image_data)
        return img
    
    
    js = "let c = document.createElement('canvas');let ctx = c.getContext('2d');" \
        "let img = document.getElementsByTagName('img')[0]; /*找到图片*/ " \
        "c.height=img.naturalHeight;c.width=img.naturalWidth;" \
        "ctx.drawImage(img, 0, 0,img.naturalWidth, img.naturalHeight);" \
        "let base64String = c.toDataURL();return base64String;"
        
    base64_str = dr.execute_script(js)
    img = base64_to_image(base64_str)


    import ddddocr

    ocr = ddddocr.DdddOcr()

    res = ocr.classification(img)
    print(res)




















    dr.find_element(By.ID,"Captcha").send_keys(res)#百度搜索框中1输入“python”
    sleep(2)
    dr.find_element(By.CLASS_NAME,"btn").click()#点击搜索
    sleep(2)
# dr.find_element(By.CSS_SELECTOR,"#kw").clear()#清空搜索框
sleep(2)
dr.quit()




# dr.execute_script("")
