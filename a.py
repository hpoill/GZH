from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By #导入By定位包

webdriver.ChromeOptions()

dr=webdriver.ChromiumEdge()
dr.get("https://www.baidu.com")

sleep(10)


dr.find_element(By.ID,"kw").send_keys("python")#百度搜索框中1输入“python”
sleep(2)
dr.find_element(By.ID,"su").click()#点击搜索
sleep(2)
dr.find_element(By.CSS_SELECTOR,"#kw").clear()#清空搜索框
sleep(2)
dr.quit()




dr.execute_script("")
# options = webdriver.ChromeOptions()
# options.add_argument('ignore-certificate-errors')

# driver = webdriver.Chrome(chrome_options=options)
# from selenium import webdriver # 从selenium导入webdriver

# from selenium.webdriver.common.by import By

# driver = webdriver.ChromiumEdge() # Optional argument, if not specified will search path.

# driver.get('https://www.baidu.com') # 获取百度页面

# inputElement = driver.find_element(By.ID,'kw')

# # inputElement = driver.find_element_by_id('kw') #获取输入框

# # searchButton = driver.find_element_by_id('su') #获取搜索按钮

# searchButton = driver.find_element(By.ID,"su")

# inputElement.send_keys("杨幂") #输入框输入"Python"

# searchButton.click() #搜索

# driver.close()
