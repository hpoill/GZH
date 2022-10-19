from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By #导入By定位包

webdriver.ChromeOptions()

dr=webdriver.ChromiumEdge()


url = "https://cn.proxy-tools.com/proxy/https"
url = "https://hidemy.name/cn/proxy-list/?type=s#list"
dr.get(url)



items = dr.find_element(By.TAG_NAME,"tbody").find_elements(By.TAG_NAME,"td")

for i,j in zip(items[::7],items[1::7]):
    print(f'{i.text}:{j.text}')