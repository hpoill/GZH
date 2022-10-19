

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By #导入By定位包
import base64
import os
import re
from io import BytesIO
from PIL import Image
import ddddocr
webdriver.ChromeOptions()

dr=webdriver.ChromiumEdge()

def base64_to_image(base64_str):
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    return img





ocr = ddddocr.DdddOcr()

def get_ocr_text(dr):
    js = "let c = document.createElement('canvas');let ctx = c.getContext('2d');" \
        "let img = document.getElementsByTagName('img')[0]; /*找到图片*/ " \
        "c.height=img.naturalHeight;c.width=img.naturalWidth;" \
        "ctx.drawImage(img, 0, 0,img.naturalWidth, img.naturalHeight);" \
        "let base64String = c.toDataURL();return base64String;"
        
    base64_str = dr.execute_script(js)
    img = base64_to_image(base64_str)
    res = ocr.classification(img)
    # print(res)
    return res

url = "https://www.poi86.com/poi/amap/province/510000.html"

dr.get(url)
sleep(1)





def get_a_list(dr,isUrl=False):
    sc_body = dr.find_elements(By.CLASS_NAME,"list-group")[1]
    a_list = sc_body.find_elements(By.TAG_NAME,"a")
    _a_list = []
    if isUrl == True:
        for a in a_list:
            _a_list.append(a.get_attribute("href").split('/')[-2])
    else:
        _a_list = a_list
    return _a_list







def go_url(a):
    href = a.get_attribute("href")
    print(a.text)
    dr.execute_script(f"""
window.open("{href}")
""")
    dr.switch_to.window(dr.window_handles[-1])

        #下载


def download_json(area_code):
    dr.get(f"https://www.poi86.com/poi/download_area_geojson/{area_code}.html")
    sleep(2)
    yzm = get_ocr_text(dr)
    dr.find_element(By.ID,"Captcha").send_keys(yzm)#百度搜索框中1输入“python”
    dr.find_element(By.CLASS_NAME,"btn").click()#点击搜索
    sleep(2)
    error = dr.find_element(By.CLASS_NAME,"alert-warning")
    if error != None and error.text == "验证码错误":
        print(error.text," ",area_code)
        download_json(area_code)



city_list = get_a_list(dr)

city_list = []

for city in city_list:
    go_url(city)
    url0 = dr.find_element(By.CLASS_NAME,"file-download").find_element(By.TAG_NAME,"a").get_attribute("href")
    url0 = url0.split('/')[-1].replace(".html", "")
    url_list = [url0] + get_a_list(dr,True)
    for a in url_list:
        # print(a)
        
        #https://www.poi86.com/poi/download_area_geojson/510104.html
        download_json(a)
    dr.close()
    dr.switch_to.window(dr.window_handles[0])

dl = ["510105","510321","510402","510500","510623","510683","510824","510900","510921","511111","511725","511921","513224","513226","513329","513334","513336","513422","513427","513429"]
dl = ["510921"]
for d in dl:
    download_json(d)


# for a in city_list:
#     city = a.get_attribute("href")
#     print(a.text)
#     dr.execute_script(f"""
#     window.open("{city}")
#     """)
#     dr.switch_to.window(dr.window_handles[-1])
#     area_list = get_a_list(dr)
#     for area in area_list:
#         _area = area.get_attribute("href")
#         print(area.text)
#         dr.execute_script(f"""
#         window.open("{_area}")
#         """)

sleep(2)

dr.quit()


