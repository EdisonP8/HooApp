from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 指定测试机是安卓还是苹果
desired_caps['platformVersion'] = '10.0.0'  # 手机操作系统的版本号
desired_caps['deviceName'] = 'M2006C3LC'  # 手机型号
desired_caps['appPackage'] = 'com.hoo.qianbao'  # 是安卓应用的包名
desired_caps['appActivity'] = 'com.hufu.qianbao.activitys.SplashActivity'
desired_caps['noReset'] = True  # noReset得作用就是不要清除应用的数据
# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 连接appium  serve
driver.implicitly_wait(5)

driver.find_element_by_id("com.hoo.qianbao:id/iv_5").click()
sleep(2)
driver.find_element_by_id("com.hoo.qianbao:id/iv_property_setting").click()
sleep(5)
input('**** Press to quit..')
driver.quit()
